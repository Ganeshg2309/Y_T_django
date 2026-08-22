from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
#here in this line we ar rendring the home.html file which is in the 
#in the templates folder of tmplates folder outsid the blog folder and if 
#you want to render the html file which is in the templates folder of the
#blog app the write "blog/home.html".

def about(request):
    return render(request, 'blog/about.html')