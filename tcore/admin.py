from django.contrib import admin
from django.http import HttpRequest

# Register your models here.


from .models import *


# admin arayüzünde modelin listelemeyeceğimiz özelikleri
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone','email','message')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=('title',)
    #yeni about içeriği ekle butonunu disable'a çekilmesi
    def has_add_permission(self, request):
        return False
    #about içeriğini silme özelliğinin disable'a çekilmesi
    def has_delete_permission(self, request, obj=None):
        return False