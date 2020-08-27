from django.shortcuts import render
from .models import Qipaoshui
# Create your views here.
def estimate(requset):
    shorts = Qipaoshui.objects.all()

    return render(requset,'index1.html',locals())