import csv
from django.core.management import BaseCommand
from MyApp1.models import teacher #This is the model we made previously, you will need to adjust this if your app or model name is different

class Command(BaseCommand):
    help = "just use it, loser"
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt', encoding='utf-8-sig') as f:
            reader = csv.reader(f, dialect='excel')
            for row in reader:
                teacher.objects.create(Name=row[0],Area=row[1])

            print('Added ' + str(count) + 'new teachers!')