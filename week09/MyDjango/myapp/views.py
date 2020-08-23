from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .form import LoginForm
from django.contrib.auth import authenticate,login


def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return render(request, 'index.html')
            else:
                return render(request, 'file.html', {'form': login_form})
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})