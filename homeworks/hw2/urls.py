from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('clients/', clients, name='clients'),
    path('products/', products, name='products'),
]