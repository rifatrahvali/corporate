# myapp/urls.py
from django.urls import path
from .views import * 
urlpatterns = [
	path('', index, name='index'),
    path('welcome/', welcome_user, name='welcome_user'),

    path('info/', website_info, name='website_info'),
]