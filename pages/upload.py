from django.shortcuts import render, HttpResponse


def index(requests):
    return render(requests, 'upload.html')