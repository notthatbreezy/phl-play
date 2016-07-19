import csv

from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
from django.utils.text import slugify

from playgrounds.models import Playground

class Command(BaseCommand):
    help = 'Import Playground Data'

    def add_arguments(self, parser):
        parser.add_argument('path_to_csv', type=str)

    def handle(self, *args, **options):
        csv_path = options['path_to_csv']
        playgrounds = []
        
        with open(csv_path, 'rb') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                print row
                if row['ASSET_SUBTYPE1'] != 'Playground':
                    continue
                name = row['SITE_NAME']
                playground = Playground(
                    point=Point(float(row['X']), float(row['Y']), srid=4326),
                    address=row['ASSET_ADDR'], name=name, slug=slugify(name)
                )
                playgrounds.append(playground)
        Playground.objects.bulk_create(playgrounds)
