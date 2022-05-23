# Files
#filename = "dataset/mbox-short.txt"
def myinput():
  fname = input("Enter file name: ")
  return(fname)
def compute(fname):
  fh = open(fname)
  count=0
  s=0
  for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
       ext=line.find(":")
       e=float(line[20:])
       s=float(s+e)
       count=count+1
  avg=float(s/count)
  return avg    
def output(avg):
  print("Average spam confidence:",avg)
def main():
  fname=myinput()
  avg=compute(fname)
  output(avg)  
main()    
