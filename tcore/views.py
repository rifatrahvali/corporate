
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#index sayfasını görüntüleyecek.

# işlem sırası
# URL talebi gelir
# views.index çalışır
# template klasöründeki index html ile tarayıcıya sayfayı yönlendirir.
def index(request):
    return render(request, 'index.html')

def merhaba(request):
	#Görünüm fonksiyonu içinde işlemleri gerçekleştirin 
    result = "Merhaba, Django!" 
	#HttpResponse ile yanıt döndürme
    return HttpResponse(result)


def welcome_user(request):
    # Kullanıcı adını simüle etmek için bir bağlam (context) oluşturuyoruz
    user_name = "Rıfat Rahvalı"
    # render fonksiyonu ile HTML şablonunu kullanarak bir HTTP yanıtı oluşturuyoruz
    return render(request, 'welcome_user.html', {'user_name': user_name})

# şablon ile html'ye birden fazla data gönderme işlemi
def website_info(request):
    context_data = {
        "name" : "Rıfat Rahvalı",
        "company" : "RRDEV",
        "website" : "rifatrahvali.com"
    }
    return render(request,'website_info.html',context_data)