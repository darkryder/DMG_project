# nominal
# ordinal
# binary
# interval
# ratio
# undecided

from app.models import TrainingDataset, make_equal_length

ABSENT_ATTRIBUTES = (218, 240)

OPTIONS = [(1, 'nominal'), (2, 'ordinal'), (3, 'binary'),
		   (4, 'interval'), (5, 'ratio'), (-1, 'undecided')]

#range_ = raw_input("Enter attribute range, for example 1-126, inclusive of attributes.")
#lower, higher = map(int, range_.split('-'))
results = {}
decisions = dict(OPTIONS)

sample_datapoints = []

def print_info():
	for x in OPTIONS:
		print "%s(%d) | " % (x[1], x[0]) ,
	print
	print "Select above options. [0 to go to previous dataset if you made a mistake][-1 if you want someone else to check]"
attr1=[]
print "Collecting data, please wait..."
for i, obj in enumerate(TrainingDataset.objects.all()):
	if i > 2000: break
	sample_datapoints.append(obj)
f1=open('undecidedAttributes.txt','r')
content = f1.readlines()
for x in content:
    attr1.append(x.strip())
att = 0
while (att < len(attr1)):
	if attr1[att] in ABSENT_ATTRIBUTES: 
		att+=1
		continue

	print "[%s]" % attr1[att]
	check = [getattr(x, "attr_" + str(attr1[att])) for x in sample_datapoints]
	if check is not None: print " | ".join([x if x is not None else "None" for x in check])
	else: print "None found, skipping"
	print_info()

	# ask for decision
	done = False
	while not done:
		choice = raw_input()
		try:
			choice = int(choice)
		except:
			print "Int please"
			continue
		if choice in [x[0] for x in OPTIONS]:
			if(choice == -1):
				results['attr_' + str(attr1[att])] = OPTIONS[5][1]
			else:
				results['attr_' + str(attr1[att])] = OPTIONS[choice-1][1]
			done = True
		elif choice == 0:
			done=True

	if choice == 0: att -= 2 # because the lower line will increment it to finally get to -=1
	att+=1

f = open('undecidedDataSet.txt', 'a+')
f.write(str(results))
f.close()
