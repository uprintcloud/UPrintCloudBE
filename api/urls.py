from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload, name='api.upload'),
    path('request', views.request, name='api.request'),
    path('download', views.download, name='api.download'),
    path('login', views.login, name='api.login'),
    path('join', views.join, name='api.join'),
]
