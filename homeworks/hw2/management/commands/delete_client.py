from django.core.management.base import BaseCommand
from hw2.models import Client


class Command(BaseCommand):
    help = "Delete user by ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = Client.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
        self.stdout.write(f'{user}')