# T
filename = "dataset/mbox-short.txt"
filehandle=open(filename)
counts={}


for l in filehandle:
	if l.startswith("From ")
		time=l.split()[5].split(":")
		counts [time] = counts.get(t[0], 0) + 1

    
lst = list()

for key, value in counts.items()
    lst.append( (key,value) )
lst.sort()

for hour, counts in lst:
    print (hour)
    print(counts)
