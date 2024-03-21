"""
URL configuration for corporate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include

#media ve static dosyaları
from django.conf.urls.static import static
from django.conf import settings

from tcore.views import *


#Tüm uygulama url adreslerini buradan yöneteceğiz.

# iş akışı
# proje url
# app url
# app view
# app model & app template
urlpatterns = [
    path('admin/', admin.site.urls),
   
    # # tcore uygulaması
    path('',include('tcore.urls'),),
    
    # # tcore uygulaması içerisindeki views
    # path('merhaba/', merhaba, name='merhaba_view'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)