from django.urls import path
from . import views
from .views import *
from django.contrib import admin
from django.conf.urls.static import static
urlpatterns = [
    path('', views.page, name="main"),
    path('<str:post_Name>/', views.page2 , name="about"),
]
'''content = views.Weather()
for i in content:
    urlpatterns.append(path(str(i["City"])[:-1], views.page2, {'current': i}, name="about"),)'''
