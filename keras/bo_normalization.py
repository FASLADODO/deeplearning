

print(' ----- hashs --------- ')

hashs = [653111801018520453196685545042507674211911431272, 
  753111801018520453196685545042507674211911431272, 
  653111801018520453196685545042507674211911431273, 
  683111801018520453196685545042507674211911431272, 
  654111801018520453196685545042507674211911431272]

bigger = 0
smaller = 0

for i in range(len(hashs)):
	if bigger < hashs[i]:
		bigger = hashs[i]
	if smaller == 0 or  smaller > hashs[i]:
		smaller = hashs[i]

#print(smaller)
#print(bigger)

for i in range(len(hashs)):
    hashs[i] = (hashs[i] - smaller) /  ( bigger - smaller )

for i in range(len(hashs)):
	print(hashs[i])



print(' ----- times --------- ')

times = [1452348009, 
  1442349009, 
  1442347009, 
  1442345009, 
  1442318009]

bigger = 0
smaller = 0

for i in range(len(times)):
    if bigger < times[i]:
	    bigger = times[i]
    if smaller == 0 or  smaller > times[i]:
	    smaller = times[i]


for i in range(len(times)):
    times[i] = (times[i] - smaller) /  ( bigger - smaller )

for i in range(len(times)):
	print(times[i])