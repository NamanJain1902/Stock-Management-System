from django.contrib import admin
from django.urls import path
from stockmngmt import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/', views.list_items, name='list_items'),
    path('add_items/', views.add_items, name='add_items'), 
    path('admin/', admin.site.urls),
]
