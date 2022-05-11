from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product-detail', views.product_detail, name='product-detail'),
    path('auth-page', views.auth_page, name='auth-page')
]