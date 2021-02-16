from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
import requests
from django.http import JsonResponse
import datetime
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.conf import settings



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('/login/')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'users/show.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # datas(request)
            return redirect('/confirm/')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'users/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

@login_required
def showMemes(request):
    PARAMS = {'box_count':5}
    r = requests.get(url = "https://api.imgflip.com/get_memes", params = PARAMS)
    jsons = r.json()
    print(jsons["data"]["memes"][0:5])
    # return render(request,'users/showJokes.html',context = {"data":jsons["data"]["memes"][0:5]})
    return render(request,'users/showJokes.html',context = {"data":jsons["data"]["memes"][0:5]})


@login_required
def confirmationPage(request):
    return render(request,'users/confirm.html')



