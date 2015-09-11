from glob import glob
from progressbar import ProgressBar
import os

from django.core.management.base import BaseCommand

TEMPLATE = """

NOMINAL = %{nominal}s
ORDINAL = %{ordinal}s
BINARY  = %{binary}s
NUMERIC = %{numeric}s

"""


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

        categories = {x: [] for x in ('nominal', 'ordinal', 'binary', 'numeric')}
        for attr_name, attr_type in final_dict.items():
            if attr_type in ('nominal', 'ordinal', 'binary'):
                categories[attr_type].append(attr_name)
            elif attr_type in ('interval', 'ratio'):
                categories['numeric'].append(attr_name)
            else:
                print "found weird", attr_type, "for", attr_name

        filename = "attribute_classifications.py"
        if os.path.exists(filename):
            os.remove(filename)
        output = open(filename, 'a+')
        f.write(TEMPLATE % categories)
