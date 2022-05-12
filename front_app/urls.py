from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product-detail/<str:pk>', views.product_detail, name='product-detail'),
    path('catagory-detail/<str:pk>', views.catagory_detail, name='catagory-detail'),
    path('auth-page', views.auth_page, name='auth-page')
]