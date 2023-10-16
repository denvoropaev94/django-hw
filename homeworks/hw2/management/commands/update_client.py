from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = "Update client name by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        user = Client.objects.filter(pk=pk).first()
        user.name = name
        user.save()
        self.stdout.write(f'{user}')