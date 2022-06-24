def myinput():
  fname=input("Enter file:")
  return fname
def compute(fname):
  f=open(fname)
  count={}  
  w2=dict()  
  for line in f
    if line.startswith("From")
      email=line.split()[1]
      count[email]=count.get(email,0)+1
  max_count=0
  max_email=0
  for email in count
    if max_count<count[email]
      max_count=count[email]
      max_email=email
  return max_count,max_email
def output(max_count,max_email)
  print(max_email,max_count)
def main():
  fname=myinput()
  max_count,max_email=compute(fname)
  output(max_count,max_count)

        
        