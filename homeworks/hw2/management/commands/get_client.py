from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = "Get client by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')
