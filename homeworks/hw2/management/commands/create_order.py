# from django.core.management.base import BaseCommand
# from hw2.models import Client, Product, Order
# from django.shortcuts import get_object_or_404
#
#
# #
# #
# class Command(BaseCommand):
#     help('Create_Order')
#
#     def add_arguments(self, parser):
#         parser.add_argument('client_id', type=int, help='UserID')
#         parser.add_argument('product_ids', type=int, help='ProductID')
#
#     def handle(self, *args, **options):
#         client = get_object_or_404(Client, pk=client_id)
#         products = Product.objects.filter(pk__in=product_ids)
#         total_price = sum(product.price for product in products)  # можно посчитать сумму заказа
#         order = Order.objects.create(customer=client, total_price=total_price)  # Создаем заказ
#         order.products.add(*products)  # Добавляем выбранные продукты в заказ
#         order.save()
#         self.stdout.write(f'{order}')
        # return HttpResponse(f"Заказ успешно создан для клиента {client.name} на сумму {total_price} рублей.")
