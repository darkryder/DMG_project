import csv

from django.core.management.base import BaseCommand
from app.models import TrainingDataset, make_equal_length

class Command(BaseCommand):
    help = 'Read csv file of training data and put it in the database'
    args = 'file_path'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *path_args, **options):
        with open(path_args[0], 'rb') as csvfile:
            csvreader = csv.reader(csvfile)
            print "starting"
            next(csvreader) # to skip the headings
            c = 0
            for counter, row in enumerate(csvreader):
                #import pdb; pdb.set_trace()
                id_ = int(row[0])
                target = int(row[-1])
                dataset = TrainingDataset.objects.create(attr_ID=id_, attr_TARGET=target)
                for x in range(1, 1934 + 1):
                    if x in (218, 240):
                        #print "Skipping", x, 'of ', counter
                        continue
                    x_temp = x
                    if 218 < x < 240: x_temp -= 1
                    if x > 240: x_temp -= 2
                    setattr(dataset, 'attr_VAR_' + make_equal_length(x_temp), row[x_temp])
                dataset.save()

                if counter % 100 == 0: print counter
                c = counter
            print "Inserted", c, "rows"
