from django.contrib import admin
from .models import *

# Register your models here.
class bookinfodata(admin.ModelAdmin):
    list_display=['id', 'title','auther','isbn','publisher']

admin.site.register(bookinfo,bookinfodata)