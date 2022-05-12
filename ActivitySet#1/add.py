#write a program to add 2 numbers using 4 fuctions
def myinput():
  s=float(input("Enter two numbers"))
  return s
def add(a,b):
  s=a+b
  sum=float(s)
  return sum
def output(s):
  print(s)
def main():
  a=myinput()
  b=myinput()
  s=add(a,b)
  output(s)
main()