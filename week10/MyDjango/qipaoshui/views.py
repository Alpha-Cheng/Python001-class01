from .models import Qipaoshui
from django.db.models import Avg
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .form import LoginForm
from django.contrib.auth import authenticate,login
# result.html



# def tables_url(requset):
#     return render(requset,'tables.html')

def login_url(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data 
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return render(request, '/index.html')
            else:
                return render(request, 'file.html', {'form': login_form})
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})

def estimate_url(requset):
    shorts = Qipaoshui.objects.all()
    # 评论数量
    counter = Qipaoshui.objects.all().count()
    # star_values = Qipaoshui.objects.values_list('n_star')
    # 平均星级
    star_avg = f" {Qipaoshui.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg = f" {Qipaoshui.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
    # 正向数量
    queryset = Qipaoshui.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()
    # 负向数量
    queryset = Qipaoshui.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()
    return render(requset,'result.html',locals())

def index_url(request):
    return render(request, 'index.html')