import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Эта команда должна прочитать CSV и записать данные в БД'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            gadget = Phone(
                name=phone.get('name'),
                price=phone.get('price'),
                image=phone.get('image'),
                release_date=phone.get('release_date'),
                lte_exists=phone.get('lte_exists'),
                slug='_'.join(phone.get('name').lower().split())
                )
            gadget.save()
            self.stdout.write(f'Телефон {gadget.name} добавлен в базу')
