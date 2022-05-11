from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"front_app/index.html", {})

def product_detail(request):
    return render(request, "front_app/product-detail.html", {})