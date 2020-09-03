from django.db import models

# Create your models here.
class Qipaoshui(models.Model):
    id = models.BigAutoField(primary_key = True)
    date = models.CharField(max_length = 30)
    n_star = models.IntegerField()
    sum_i = models.IntegerField()
    link = models.CharField(max_length=40)
    estimate = models.CharField(max_length=200)
    sentiment = models.DecimalField(max_digits=11,decimal_places = 10)