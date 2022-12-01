from django.shortcuts import render
from django.http import HttpResponse


def index(request, id):
    return HttpResponse("Hello World! このページは投稿のインデックスです。" + str(id))


def hello(request):
    return HttpResponse("Hello World")


# Create your views here.
