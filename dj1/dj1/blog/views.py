from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("wellcome home")

def about(request):

    a=10+50
    return HttpResponse(f"about is {a}")
# Create your views here.   
