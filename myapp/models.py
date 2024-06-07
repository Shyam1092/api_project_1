from django.db import models

# Create your models here.

class bookinfo(models.Model):
    title=models.CharField(max_length=50)
    auther=models.CharField(max_length=50)
    isbn=models.CharField(max_length=50) #international standerd book number
    publisher=models.CharField(max_length=50)