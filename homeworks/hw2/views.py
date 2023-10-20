from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm


def index(request):
    return render(request, 'hw2/index.html')


def clients(request):
    users = Client.objects.all()
    return HttpResponse(users)


# def products(request):
#     prs = Product.objects.all()
#     return HttpResponse(prs)


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


def add_client(request):
    form = ClientForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        message = 'Ошибка в данных'
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        image = form.cleaned_data['image']
        fs = FileSystemStorage()
        fs.save(image.name, image)
        address = form.cleaned_data['address']
        client = Client(name=name, email=email, phone_number=phone_number, image=image, address=address)
        client.save()
        message = 'Клиент сохранен'
    else:
        form = ClientForm()
        message = 'Заполните форму'
    return render(request, 'hw2/add_client.html', {'form': form, 'message': message})


def get_all_products(request):
    products = Product.objects.all()
    return render(request, 'hw2/products.html', {'products': products})


def change_product(request, product_id):
    product = Product.objects.filter(pk=product_id).first()
    form = ProductForm(request.POST, request.FILES)
    if request.method == 'POST' and form.is_valid():
        image = form.cleaned_data['image']
        if isinstance(image, bool):
            image = None
        if image is not None:
            fs = FileSystemStorage()
            fs.save(image.name, image)
        product.name = form.cleaned_data['name']
        product.description = form.cleaned_data['description']
        product.price = form.cleaned_data['price']
        product.count_product = form.cleaned_data['count_product']
        product.image = image
        product.save()
        return redirect('products')
    else:
        form = ProductForm(initial={'name': product.name, 'description': product.description,
                                    'price': product.price, 'count_product': product.count_product,
                                    'image': product.image})

    return render(request, 'hw2/change_product.html', {'form': form})
