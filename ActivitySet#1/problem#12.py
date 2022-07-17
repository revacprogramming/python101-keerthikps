# RegEx
# https://www.py4e.com/lessons/regex
import re
filename=('dataset/mbox-short.txt')
fhand=open(file)
number=list()
for line in fhand:
    l=line.rstrip()
    nums = re.findall('[0-9]+',l)
    for i in nums:
        num=int(i)
        number.append(num)
    
print(sum(number))
