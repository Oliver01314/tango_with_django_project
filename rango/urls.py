from unicodedata import name
from django.urls import path
from rango import views

app_name = 'rango'

# 'about/' means plus about/ to show about page
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name = 'about'),
    ]


