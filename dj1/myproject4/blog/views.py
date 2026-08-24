from django.shortcuts import render

def view1(request):
    return render(request, 'blog/base.html')


# Create your views here.
