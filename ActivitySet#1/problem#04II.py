#conditional execution 2
def myinput():
  score = input("Enter Score: ")
  s =  float(score)
  return s  
def compute(s): 
  x = "NULL"
  if s>0.0 and s<1.0:
    if s >= 0.9 and s<=1.0:
	    x = 'A'
    elif s >=0.8:
	    x='B'
    elif s >=0.7:
	    x='C'
    elif s >= 0.6:
	    x='D'
    else:
	    x ='F'
  else:
    x ="Out of Range"
  return x
def output(x):
  print (x)
def main():
  s=myinput()
  x=compute(s)
  output(x)
main()