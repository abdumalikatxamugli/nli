from django.shortcuts import render


# Create your views here.

def general(request):
    return render(request, 'aboutus/index.html')


def license(request):
    return render(request, 'aboutus/license.html')


def management(request):
    return render(request, 'aboutus/management.html')


def reports(request):
    return render(request, 'aboutus/reports.html')