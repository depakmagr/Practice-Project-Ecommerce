from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello Deeps!!</h1>")


def shop(request):
    return HttpResponse("<h1>This is my shop!!</h2>")