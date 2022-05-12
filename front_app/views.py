from django.http import HttpResponse
from django.shortcuts import render

from front_app.models import Catagory, Product, Service, TeamMember, Testimonial
from .constants import about_info_body, about_information
# Create your views here.

def index(request):
    catagories = Catagory.objects.all()
    service_list = Service.objects.all()
    team_member = TeamMember.objects.all()
    testimonials = Testimonial.objects.all()
    product_list = Product.objects.all()

    index_data = {
        'about_body': about_info_body,
        'about_list_info' : about_information,
        'catagory_list' : catagories,
        'service_list' : service_list,
        'team_member' : team_member,
        'testimonials' : testimonials,
        'product_list' : product_list,
    }
    return render(request,"front_app/index.html", context=index_data)

def product_detail(request, pk):
    catagories = Catagory.objects.all()
    service_list = Service.objects.all()
    product_list = Product.objects.get(pk=pk)
    print(product_list)
    context_data = {
        'catagory_list': catagories,
        'service_list': service_list,
        'product_list': [product_list]
    }
    return render(request, "front_app/product-detail.html", context=context_data)

def catagory_detail(request, pk):
    catagories = Catagory.objects.all()
    service_list = Service.objects.all()
    catagory = Catagory.objects.get(pk=pk)
    product_list = Product.objects.filter(catagory=catagory)
    print(product_list[0].productimage_set.all())
    context_data = {
        'catagory_list': catagories,
        'service_list': service_list,
        'product_list': product_list
    }
    return render(request, "front_app/product-detail.html", context=context_data)

def auth_page(request):
    return render(request,"front_app/auth.html",context={})