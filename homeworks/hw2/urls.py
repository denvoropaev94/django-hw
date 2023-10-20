from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('clients/', clients, name='clients'),
    path('create_order/<int:client_id>/<str:product_ids>/', create_order, name='create_order'),
    path('client_orders/<int:client_id>/', client_orders, name='bask'),
    path('client_sorted/<int:client_id>/<int:days_ago>/', sorted_basket, name='sorted_basket'),
    path('add_client/', add_client, name='add_client'),
    path('products/', get_all_products, name='products'),
    path('change_product/<int:product_id>/', change_product, name='change_product'),

]
