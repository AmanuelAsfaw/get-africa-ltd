from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"front_app/index.html", {})