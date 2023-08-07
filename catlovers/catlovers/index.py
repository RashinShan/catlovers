from django.http import HttpResponse
from django.shortcuts import render

def homepage1(request):
    return render(request,'homepage.html')

def aboutus2(request):
    return render(request,'aboutus.html')