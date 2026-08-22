from django.shortcuts import render
from django.http import HttpResponse

def post_details(request,post_id):
    return HttpResponse(f'this is post details page of post id {post_id}')
def user_profile(request,username):
    return HttpResponse(f'this is  user profile view and user name is {username}')
def article_by_year(request,years):
    return HttpResponse(f'this is article by year view and year is {years}')
#def article_details(request,years,month):
#   return HttpResponse(f'this is article details view and year is {years} and month is {month}')
# so above two lines of code are commented because we can use **kwards to get the values of years and month in the view function. so we can use **kwards instead of years and month in the view function.
def article_details(request, **kwards):
    return HttpResponse(f'data: {kwards}')
