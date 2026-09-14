from django.shortcuts import render
from datetime import datetime

class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def home(request):
    context = {
        "name": ganesh,
        "age":23,
        "shills":["python","django","html"],
        "user": user("sadashiv",23),
        "blog":{
            "title":"Harrypotter"
            "artists" : "harsha"
            "created_at":datetime(2025,8,2,3,10)
            },
        "empty_value":None,
    }
return render(request,"blog/home.html",context)



# Create your views here.
