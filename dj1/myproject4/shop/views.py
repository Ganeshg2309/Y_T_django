from django.shortcuts import render

def view1(request):
    return render(request, 'shop/base.html',)
