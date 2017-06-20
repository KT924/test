from django.shortcuts import render
from test import select
def first(request):
    huowu=select.value1()
    shu=select.value2()
    return render(request,'first.html',{'huowu':huowu,'shuliang':shu})

def index(request):
    huowu=select.value1()
    shu=select.value2()
    return render(request,'index.html',{'huowu':huowu,'shuliang':shu})
# Create your views here.
