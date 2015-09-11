from glob import glob
from progressbar import ProgressBar

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Create a main attribute file after merging all small attribute files'

    def handle(self, *args, **options):
        final_dict = {}
        files = glob("attr_*")
        if len(files) == 0:
            print "No files found to merge"
            return
        pbar = ProgressBar(maxval=len(files) - 1).start()
        for i, filename in enumerate(files):
            with open(filename, 'r') as f:
                data = f.read()
                subset = eval(data) # hope no one is evil
                final_dict.update(subset)
                pbar.update(i)
        pbar.finish()
        print final_dict, len(final_dict)
