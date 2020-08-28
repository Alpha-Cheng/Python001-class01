from django.db import models

# Create your models here.
class Qipaoshui(models.Model):
    id = models.BigAutoField(primary_key=True)
    collect = models.IntegerField()
    estimate = models.TextField()
    sentiment = models.FloatField( )