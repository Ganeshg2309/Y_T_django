from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse(" this is a home page of shop app")
def about(request):
    return HttpResponse(" this is a about page of shop app")
# Create your views here.
