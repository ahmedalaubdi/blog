from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse("The main page")

    
def index(reques):
    return HttpResponse("Welcome to products")
