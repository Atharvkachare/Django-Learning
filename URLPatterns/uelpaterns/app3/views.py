from django.shortcuts import render
from django.HttpResponse import HttpResponse

# Create your views here.

def myapp3(req):
    return HttpResponse("<h1>Hello My App 3<h1/>")
