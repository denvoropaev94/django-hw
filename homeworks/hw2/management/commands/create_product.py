from django.core.management.base import BaseCommand
from hw2.models import Product


class Command(BaseCommand):
    help('Create_user')

    def handle(self, *args, **kwargs):
        # pr1 = Product(name=' Iphone15pro', description='The best phone in the world', price='2000',
        # count_product='15')
        # pr2 = Product(name=' Iphone15promax', description='The best phone in the world', price='3000',
        #               count_product='15')
        pr3 = Product(name=' iphone11', description='The best in the world', price='600',
                      count_product='50')
        pr3.save()
        self.stdout.write(f'{pr3}')
