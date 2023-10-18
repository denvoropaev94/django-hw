from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Client, Product, Order


def index(request):
    return render(request, 'hw2/index.html')


def clients(request):
    users = Client.objects.all()
    return HttpResponse(users)


def products(request):
    prs = Product.objects.all()
    return HttpResponse(prs)


def create_order(request, client_id, product_ids):
    client = get_object_or_404(Client, pk=client_id)
    products = Product.objects.filter(pk__in=product_ids)
    total_price = sum(product.price for product in products)  # можно посчитать сумму заказа
    order = Order.objects.create(customer=client, total_price=total_price)  # Создаем заказ
    order.products.add(*products)  # Добавляем выбранные продукты в заказ
    return HttpResponse(f"Заказ успешно создан для клиента {client.name} на сумму {total_price} рублей.")


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client)
    products = []
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'hw2/client_orders.html', {'client': client, 'orders': orders, 'products': products})


def sorted_basket(request, client_id, days_ago):
    products = []
    product_set = []
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(customer=client, date_ordered__range=(before, now)).all()
    for order in orders:
        products = order.products.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)

    return render(request, 'hw2/client_all_product.html',
                  {'client': client, 'product_set': product_set, 'days': days_ago})
