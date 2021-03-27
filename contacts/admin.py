from django.contrib import admin
from .models import *
from django import forms
from treasuremap.forms import LatLongField
from treasuremap.widgets import AdminMapWidget
from modeltranslation.admin import TranslationAdmin


# Register your models here.
class BranchAdminForm(forms.ModelForm):
    longitude = forms.DecimalField(required=False)
    latitude = forms.DecimalField(required=False)
    location_type = forms.ChoiceField(choices=[
        ('Map', 'Map'),
        ('Coordinates', 'Coordinates'),
    ])

    def __init__(self, *args, **kwargs):
        # only change attributes if an instance is passed
        instance = kwargs.get('instance')

        if instance:
            self.base_fields['longitude'].initial = str(instance.location).split(";")[0]
            self.base_fields['latitude'].initial = str(instance.location).split(";")[1]
        forms.ModelForm.__init__(self, *args, **kwargs)


@admin.register(Branch)
class BranchAdmin(TranslationAdmin):
    list_display = ('title',)
    fields = ('title', 'address',
              'phone_number', 'start_time',
              'end_time', 'location_type',
              'location', 'longitude', 'latitude')

    form = BranchAdminForm

    def save_model(self, request, obj, form, change):
        if form.cleaned_data['location_type'] == 'Coordinates':
            obj.location = str(form.cleaned_data['longitude']) + ";" + str(form.cleaned_data['latitude'])
        obj.save()



