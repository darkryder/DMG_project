import csv

from django.core.management.base import BaseCommand
from app.models import BaseModel, make_equal_length

class Command(BaseCommand):
    help = 'Read csv file of training data and put it in the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        with open(options['file_path'], 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            print "starting"
            next(csvreader) # to skip the headings
            counter = 0
            for row in csvreader:
                id_ = int(row[0])
                target = int(row[-1])
                dataset = BaseModel.objects.create(attr_ID=id_, target=target)
                for x in range(1, 1934 + 1):
                    setattr(dataset, make_equal_length(x), row[x])
                dataset.save()
                counter += 1

                if counter % 10000 == 0: print counter
            print "Inserted", counter, "rows"
