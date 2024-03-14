from django.shortcuts import render

# Create your views here.


#index sayfasını görüntüleyecek.

# işlem sırası
# URL talebi gelir
# views.index çalışır
# template klasöründeki index html ile tarayıcıya sayfayı yönlendirir.
def index(request):
    return render(request, 'index.html')