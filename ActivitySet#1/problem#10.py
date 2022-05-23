def myinput():
    fname = input("Enter file name: ")
    return fname
def compute(fname):
  f=open(fname)
  li=list()  
  for line in f:
    if line.startswith("From"): 
      l=line.split() 
      li.append(l)
      for i in li:
            print(i[1])
  #print(li)      #for w in l:
        #print(w[1])
        #li.append(w)      
  #return li       
#def output(li): 
 # count=0
  #for w in li:    
   # count=count+1    
    #print(w[1])
 # print("There were",count, "lines in the file with From as the first word")
def main():
  fname=input()
  li=compute(fname)
  #output(li)
main()    

