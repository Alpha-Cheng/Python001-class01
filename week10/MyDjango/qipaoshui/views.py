from .models import Qipaoshui
from django.db.models import Avg
from django.shortcuts import render
# Create your views here.
def estimate(requset):
    shorts = Qipaoshui.objects.all()

    # 评论数量
    counter = Qipaoshui.objects.all().count()

    # star_values = Qipaoshui.objects.values_list('collect')
    


    # 平均星级
    star_avg = f" {Qipaoshui.objects.aggregate(Avg('collect'))['collect__avg']:0.1f} "
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