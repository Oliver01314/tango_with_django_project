from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

#use<a href='/rango/about/'>About</a> to provide URL
def index(request):
 return HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a>")

def about(request):
 return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>")

