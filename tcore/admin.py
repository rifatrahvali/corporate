from django.contrib import admin

# Register your models here.


from .models import *


# admin arayüzünde modelin listelemeyeceğimiz özelikleri
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name','phone','email','message')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display=('title',)