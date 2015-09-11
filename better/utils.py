import csv
from progressbar import ProgressBar

PATH = "train.csv"
ROW_COUNT = 145231
ABSENT_ATTRIBUTES = (218, 240)

class Row(object):
    def __repr__(self):
        return "<%s>" % getattr(self, 'id_', 'default')

def get_data(limit=None):
    """Read csv file of training data and put it in the database"""

    if limit is not None:
        limit = min(ROW_COUNT, int(limit))
    else:
        limit = ROW_COUNT

    # pbar = ProgressBar(maxval=limit).start()
    with open(PATH, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # to skip the headings

        final_data = []
        for counter, row in enumerate(csvreader):
            if counter == limit - 1: break

            datapoint = Row()
            datapoint.id_ = int(row[0])
            datapoint.target = int(row[-1])

            for x in range(1, 1934 + 1):
                if x in ABSENT_ATTRIBUTES: continue
                x_temp = x
                if 218 < x < 240: x_temp -= 1
                if x > 240: x_temp -= 2
                setattr(datapoint, 'VAR_' + _make_equal_length(x), row[x_temp])
            yield datapoint
            # pbar.update(counter)
        
        # pbar.finish()

def _make_equal_length(a):
    return '0'*(4-len(str(a))) + str(a)
