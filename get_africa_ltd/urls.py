"""get_africa_ltd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (handler400, handler403, handler404, handler500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('front_app.urls'), name='front_app')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = "get_africa_ltd.views.page_403_not_found_view"
handler404 = "get_africa_ltd.views.page_404_not_found_view"
# handler500 = "get_africa_ltd.views.page_500_not_found_view"