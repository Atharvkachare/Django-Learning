from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request.user)
    
    return HttpResponse("Welcome to the Polls app!")
