from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.upload, name='api.upload'),
    path('request', views.request, name='api.request'),
]
