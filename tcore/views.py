
from typing import Any
from django.shortcuts import render
from django.http import HttpResponse

### REDIRECT Ekle
from django.shortcuts import redirect




# # Create your views here.


# #index sayfasını görüntüleyecek.

# # işlem sırası
# # URL talebi gelir
# # views.index çalışır
# # template klasöründeki index html ile tarayıcıya sayfayı yönlendirir.
# def index(request):
#     return render(request, 'index.html')

# def merhaba(request):
# 	#Görünüm fonksiyonu içinde işlemleri gerçekleştirin 
#     result = "Merhaba, Django!" 
# 	#HttpResponse ile yanıt döndürme
#     return HttpResponse(result)

# def goToGoogleView(request):
#     return redirect("https://www.google.com.tr/")

# def welcome_user(request):
#     # Kullanıcı adını simüle etmek için bir bağlam (context) oluşturuyoruz
#     user_name = "Rıfat Rahvalı"
#     # render fonksiyonu ile HTML şablonunu kullanarak bir HTTP yanıtı oluşturuyoruz
#     return render(request, 'welcome_user.html', {'user_name': user_name})

# # şablon ile html'ye birden fazla data gönderme işlemi
# def website_info(request):
#     context_data = {
#         "name" : "Rıfat Rahvalı",
#         "company" : "RRDEV",
#         "website" : "rifatrahvali.com"
#     }
#     return render(request,'website_info.html',context_data)

# ### DETAY ÖRNEKLERİ ###

# #slug ile detay sayfası
# #http://127.0.0.1:8000/category/1/
# def category_detail_view(request, category_slug):
#     # Burada, kategori adını ve slug'ı kullanarak gerekli veritabanı sorgularını yapabilirsiniz
#     # Şu anlık sadece alınan değerleri gösteriyoruz
#     return render(request, 'category_detail.html',{'category_name': category_slug})


# def category_detail_view_with_id(request, category_id):
# # Burada, kategori ID'sini kullanarak gerekli veritabanı sorgularını yapabilirsiniz
# # Şu anlık sadece alınan değeri gösteriyoruz
#     return render(request, 'category_detail_with_id.html',{'category_id': category_id})

# def category_detail_view_with_name(request, category_name):
#     #soldaki kategori_ismi templatede bulunan html'e gönderiliyor
#     #template içerisinde değişkene aktarılıyor
#     return render(request,"category_detail_with_name.html",{"category_name":category_name})

# ### TEMPLATE VIEW ORNEGI ###
# class MyTemplateView(TemplateView):
#     template_name = "indexTemplate.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["message"] = "TemplateView özelliği ile kulanıldı." 
#         return context

# ### TEMPLATE VIEW
from django.views.generic import TemplateView , ListView , DetailView

from .models import *

from tcore.models import *

# from django.views.generic import BaseView, ListView

# TemplateView ile vtden görsel çekme
# class IndexView(TemplateView):
#     template_name="index.html"
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['sliders'] = Slider.objects.all()
#         return context

# ListView ile vtden görsel çekme
class IndexView(ListView):
    template_name="index.html"
    context_object_name = 'sliders'
    #Slider modelinden geliyor.
    queryset = Slider.objects.all()
    #for döngüsü ile verileri template'e aktaralım.

    #index sayfasındaki hakkımızda bölümüne veri aktarımı
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Abouts'] = About.objects.first()
        #contexti Services modelin aldık 
        #index html'e Services ile hepsini gönderdik
        #for ile herbir service'i döndürdük
        context['Services'] = Services.objects.all()
        context['Blogs'] = Blog.objects.all()
        return context

class AboutView(TemplateView):
    template_name="abouts.html"
    #about sayfasındaki hakkımızda bölümüne veri aktarımı
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Abouts'] = About.objects.first()
        return context

class ServicesView(TemplateView):
    template_name="services.html"

class BlogsView(ListView):
    template_name="blogs.html"
    context_object_name = 'Blogs'
    queryset = Blog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Categories'] = Category.objects.all()
        return context

class ContactsView(TemplateView):
    template_name="contacts.html"



