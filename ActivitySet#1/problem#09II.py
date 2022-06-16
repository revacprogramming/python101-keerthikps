 #mbox-short.txt file name
#From stephen.marquard@uct.ac.za example
def myinput():
  
  fname = input("dataset/mbox-short.txt")
  return fname

  
def compute(fname):
  count=0  
  f=open(fname) 
  word=list()
  for line in f:
    if line.startswith("From "): 
      w=line.split() 
      word.append(w[1])  
      count=count+1  
  return word,count 
  
  
def output(word,count):
  for i in word:  
    print(i)
  print("There were",count, "lines in the file with From as the first word")

  
def main():
  fname=input()
  word,count=compute(fname)
  output(word,count)
main()    
