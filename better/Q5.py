from progressbar import ProgressBar
from heapq import heappop, heappush
from utils import get_data, _make_equal_length

all_data = get_data()

ROW_COUNT = 145231
LIMIT = 15
_heap = []
pbar = ProgressBar(maxval=ROW_COUNT).start()

def count_null_values(dataset):
    null = 0
    for k, v in vars(dataset).items():
        if v == "NA": null+=1
    return null

first = next(all_data)
heappush(_heap, (count_null_values(first), first))

for i, dataset in enumerate(all_data):
    count = count_null_values(dataset)
    if (count, dataset) <= _heap[0]: continue

    heappush(_heap, (count, dataset))

    if len(_heap) > LIMIT:
        _ = heappop(_heap)

    pbar.update(i)

pbar.finish()
print _heap



