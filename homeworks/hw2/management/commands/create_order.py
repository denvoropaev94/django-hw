from django.core.management.base import BaseCommand
from hw2.models import Client, Product, Order


class Command(BaseCommand):
    help('Create_Order')

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID')
        parser.add_argument('pk', type=int, help='ProductID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        product = Product.objects.filter(pk=pk).first()
        order1 = Order(customer=client, products=product, total_price='600')
        # order1.products.add(*client)
        # order1.save()
        self.stdout.write(f'{order1}')
