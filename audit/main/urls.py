from django.urls import path
from .views import index, about, clients, contacts, news, zayavka

urlpatterns = [
    path('', index, name='home'),
    path('about', about, name='about'),
    path('clients', clients, name='clients'),
    path('contacts', contacts, name='contacts'),
    path('news', news, name='news'),
    path('zayavka', zayavka, name='zayavka'),
]
