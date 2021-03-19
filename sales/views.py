from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as dj_auth, logout as dj_logout


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        print('already')
    if request.method == 'GET':
        data = {}
        template = loader.get_template('login.html')
        return HttpResponse(template.render(data, request))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_auth(request, user)
            print('pass')
        else:
            print('failed')

        return redirect('sales.login')

def logout(request):
    dj_logout(request)
    return redirect('sales.login')