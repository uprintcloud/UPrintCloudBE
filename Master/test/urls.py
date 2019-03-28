from django.urls import path
from Master.test import views

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('init', views.init),
    path('login', views.login, name='login'),
    path('join', views.join, name='join'),
    path('', views.index, name='index'),
]