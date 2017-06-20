from django.db import models

class Test(models.Model):
    X=models.CharField(max_length=50)
    Y=models.CharField(max_length=10)
# Create your models here.
