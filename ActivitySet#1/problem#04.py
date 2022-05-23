# Conditional Execution
def compute(h,r):
  if h<40:
    m=h*r
  elif h>40:
    m=40*r+(h-40)*1.5*r
  return m  
def output(m):
  print(m)
def main():
  hrs = input("Enter hours? ")
  h=float(hrs)
  rate=input("Enter the Rate")
  r=float(rate)
  m=compute(h,r)
  output(m)
main()  