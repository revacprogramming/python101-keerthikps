def myinput()
  file=input("Enter a file")
  return file
def compute(file):
  count={}
  filehandle=open(filename)
  for line in filehandle:
    words=line.split()
    if line.startswith("From") and len(words)>3 :
      w=words[1]
      count[w]=count.get(w,0)+1  
  maxword=0
  maxcount=0
  for w in count:
    if maxcount<count[w]:
      maxword=w
      maxcount=count[w]
  return maxword,maxcount
def output(maxword,maxcount):
  print(maxword,maxcount)
def main()
  file=myinput()
  maxword,maxcount=compute(file)
  output(maxword,maxcount)
main()
            
      
        
        
