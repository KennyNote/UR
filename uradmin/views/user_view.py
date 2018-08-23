# Author:Sunny Liu
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import hashlib,os
from uradmin.forms import UserForm
import json

# Create your views here.


"""
    @id : 1
    @name : register
    @author : 刘旭阳
    @date : 2018.3.12
    @describe :注册后台管理

"""
@csrf_exempt
def register(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['userpswd']
            print(username+"  "+password)
            user = auth.authenticate(username = username,password = password)
            print(user)
            if user:
                context['userExit']=True
                return render(request, 'register.html', context)
            user = User.objects.create_user(username=username, password=password)
            user.save()
            request.session['username'] = username
            auth.login(request, user)
            return redirect('/')
    else:
        context = {'isLogin':False}
    return  render(request,'register.html',context)

"""
    @id : 2
    @name : login
    @author : 刘旭阳
    @date : 2018.3.12
    @describe : 登录后台管理

"""
@csrf_exempt
def login(request):
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpswd = form.cleaned_data['userpswd']
            user = authenticate(username = username,password = userpswd)
            if user:
                auth.login(request,user)
                request.session['username'] = user
                return render(request, 'ur_admin/index.html')
            else:
                context = {'isLogin': False,'pawd':False}
                return render(request, 'login.html', context)
    else:
        context = {'isLogin': False,'pswd':True}
    return render(request, 'login.html', context)

#登出
def logout(request):
    auth.logout(request)
    return redirect('/')