import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phone_list = list(csv.DictReader(file, delimiter=';'))

        for item in phone_list:
            Phone.objects.create(
                id=item['id'],
                name=item['name'],
                image=item['image'],
                price=item['price'],
                release_date=item['release_date'],
                lte_exists=item['lte_exists']
            )
