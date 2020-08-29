from django.db import models

# Create your models here.
class Qipaoshui(models.Model):
    id = models.BigAutoField(primary_key=True)
    n_star = models.IntegerField(max_length=30)
    estimate = models.TextField()
    sentiment = models.DecimalField(max_digits=11,decimal_places=10)