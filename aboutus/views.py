from django.shortcuts import render
from .models import *

# Create your views here.

def general(request):
    history = History.objects.all()
    context = {
        'history': history
    }
    return render(request, 'aboutus/index.html', context)


def license(request):
    certificate = Certificate.objects.all()
    context = {
        'certificates': certificate
    }
    return render(request, 'aboutus/license.html', context)


def management(request):
    management = Management.objects.all()
    context = {
        'management': management
    }
    return render(request, 'aboutus/management.html', context)


def reports(request):
    reports = FinancialReport.objects.all()
    context = {
        'reports': reports
    }
    return render(request, 'aboutus/reports.html', context)