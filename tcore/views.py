
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
	# Görünüm fonksiyonu içinde işlemleri gerçekleştirin 
    result = "Merhaba, Django!" 
	# HttpResponse ile yanıt döndürme
    return HttpResponse(result)
