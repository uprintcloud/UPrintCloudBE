from django.urls import path
from Master.test import views

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('init', views.init),
    path('login', views.login, name='login'),
    path('join', views.join, name='join'),
    path('print', views.printer, name='print'),
    path('', views.index, name='index'),
]