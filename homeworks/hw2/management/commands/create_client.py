from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help('Create_user')

    def handle(self, *args, **kwargs):
        # client = Client(name=' Oleg', email='olegka@gmail.com', phone_number='8989898', address='vtb')
        client = Client(name=' Den', email='denvorop@gmail.com', phone_number='8989898', address='vtb')
        # client = Client(name=' Nikita', email='nikitka@gmail.com', phone_number='1234567', address='vtb')
        # client = Client(name=' Sasha', email='sahsa@gmail.com', phone_number='9898325', address='vtb')
        # client = Client(name=' Mark', email='markun@gmail.com', phone_number='46456435', address='vtb')
        # client = Client(name=' Matvey', email='matv@gmail.com', phone_number='21901837', address='vtb')
        client.save()
        self.stdout.write(f'{client}')
