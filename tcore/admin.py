from tkinter import commondialog
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
    
@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    group_fieldsets = True


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title','image',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','category',)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    #settings modelinde içeriği ekle butonunu disable'a çekilmesi
    def has_add_permission(self, request):
        return False
    #settings modelinde içeriğini silme özelliğinin disable'a çekilmesi
    def has_delete_permission(self, request, obj=None):
        return False
    