from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product-detail/<str:pk>', views.product_detail, name='product-detail'),
    path('catagory-detail/<str:pk>', views.catagory_detail, name='catagory-detail'),
    path('auth-page', views.auth_page, name='auth-page'),
    path('register', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login_request', views.login_view, name='login-request'),
    path('logout_request', views.logout_view, name='logout-request'),
    path('send_message', views.send_message, name='send-message'),
    path('messages', views.messages_page, name='messages-page'),
]