# myapp/urls.py
from django.urls import path
from .views import * 
urlpatterns = [
	path('', index, name='index'),
    path('welcome/', welcome_user, name='welcome_user'),

    path('info/', website_info, name='website_info'),
    #name
    path('category/<str:category_name>/', category_detail_view_with_name, name='category_detail_with_name'),

    #http://127.0.0.1:8000/category/1/
    path('category/<int:category_id>/', category_detail_view_with_id, name='category_detail_with_id'),

    #name de alıyor id'de
    path('category/<slug:category_slug>/', category_detail_view, name='category_detail'),
    
]