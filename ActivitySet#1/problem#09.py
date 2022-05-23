# List
#filename = "dataset/romeo.txt"
def myinput():
  fname = input("Enter file name: ")
  return fname
def compute(fname):
  f=open(fname)
  li=list()  
  for line in f:
    l=line.split()
    for w in l:
      if w not in li:
        li.append(w)
  return li
def output(li):
  li.sort()
  print(li)  
def main():
  fname=myinput()
  li=compute(fname)
  output(li)
main()    
        
    