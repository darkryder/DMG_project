import math
from utils import get_data, _make_equal_length
from attribute_classifications import NUMERIC as NUMERIC_ATTRIBUTES
from progressbar import ProgressBar

# The question is to calculate the attributes with the maximum dispersion.
# Since it's almost impossible to store the complete data in any form in
# the memory all at once, I'll have to calculate the dispersion in a
# streaming fashion. The dispersion I choose was standard deviation, because
# its a lot better than a simple `range` dispersion measure, also its
# extremely simple to compute in a streaming fashion.

ABSENT_ATTRIBUTES = (218, 240)
ATRIBUTES_LENGTH = 1934
ROW_COUNT = 145231

# Let's forget about the 0 index and the ABSENT_ATTRIBUTES indices
# I'll discard them in the end
all_info = [[0, 0, 0, 0] for _ in xrange(0, ATRIBUTES_LENGTH + 1)]

# For calculating the standard deviation in a streaming fashion,
# It's just necessary to store 3 variables as explained here:
# http://stackoverflow.com/a/5543790/2851353. So, the first 3 elements
# of the smaller list within all_info would be these values. The fourth
# element would be the std_dev computed till that step.
# Since, all attributes are independent, I can apply this streaming step
# on all attributes at once.

rows = get_data()
pbar = ProgressBar(maxval=ROW_COUNT - 1).start()

for i, row in enumerate(rows):
	for attr_name in NUMERIC_ATTRIBUTES:
		if i in ABSENT_ATTRIBUTES: continue
		attribute_info = all_info[int(attr_name[-4:])]
		try:
			value = float(getattr(row, attr_name))
		except ValueError, e:
			if 'domain' in e.message:
				print e
				# import pdb; pdb.set_trace()
			continue
		attribute_info[0] += 1
		attribute_info[1] += value
		attribute_info[2] += value**2
		s0, s1, s2 = attribute_info[:3]

		# if s0 not in (0, 1) and (s0 * s2) >= (s1 * s1):
		# 	attribute_info[3] = math.sqrt((s0 * s2 - s1 * s1)/(s0 * (s0 - 1)))
	pbar.update(i)

# Let's see if this dramatically improves the speed.
for info in all_info:
	s0, s1, s2 = info[:3]
	if s0 not in (0, 1) and (s0 * s2) >= (s1 * s1):
			info[3] = math.sqrt((s0 * s2 - s1 * s1)/(s0 * (s0 - 1)))

pbar.finish()

EMPTY_RESPONSE = [0, 0, 0, 0]
THRESHOLD_MINIMUM_NUMBER_OF_VALUES = 140000
filtered = [x for x in all_info if (x != EMPTY_RESPONSE and
			x[0] > THRESHOLD_MINIMUM_NUMBER_OF_VALUES)]

filtered = sorted(filtered, key=lambda x: x[3], reverse=True)

print filtered[0], all_info.index(filtered[0])

f = open("Q4_output.txt", 'w')
f.write("DISPERSION, ID\n")
for x in filtered[:10]:
    f.write("%d %s\n", x[3], str(all_info.index(x)))
f.close()