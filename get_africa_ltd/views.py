from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,"front_app/index.html", {})

def page_403_not_found_view(request, exception):
    return render(request, 'front_app/404.html', status=403)
    
def page_404_not_found_view(request, exception):
    return render(request, 'front_app/404.html', status=404)
    
def page_500_not_found_view(request, exception):
    return render(request, 'front_app/404.html', status=500)