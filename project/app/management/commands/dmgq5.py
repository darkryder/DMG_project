# nominal
# ordinal
# binary
# interval
# ratio
# undecided

from app.models import TrainingDataset, make_equal_length

ABSENT_ATTRIBUTES = (218, 240)


range_ = raw_input("Enter attribute range, for example 1-126, inclusive of attributes.")
lower, higher = map(int, range_.split('-'))
results =[]

sample_datapoints = []

print "Collecting data, please wait..."
for i, obj in enumerate(TrainingDataset.objects.all()):
    if i > 500: break
	sample_datapoints.append(obj)

att = lower
while (att <=higher):
    count=0
    if att in ABSENT_ATTRIBUTES: 
        att+=1
        continue
    check = [getattr(x, 'attr_VAR_' + make_equal_length(att)) for x in sample_datapoints]
    for x in check:
        if x=='NA': count+=1
		
    results.append(count)
    att+=1

f = open('q5.txt', 'a+')
f.write(str(results))
f.write('\n')
f.write(max(results))
f.close()
