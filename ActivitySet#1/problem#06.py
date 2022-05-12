# Loops & Iterators
def myinput():
  num = input("Enter a number: ")
  return num
def large(n):
   largest = None
   try:
      num = int(num)
      if largest is None or largest < num:
          largest = num
          return largest
    except:
      largest=0
      print ("Invalid input")
def small(n):
   smallest = None
   try:
     num = int(num)
     if smallest is None or smallest > num: 
        smallest = num
        return smallest
    except:
        smallest=0
        print ("Invalid input")
def output(l,s):
  if l!=0 and s!=0
    print ("Maximum is",largest)
    print ("Minimum is",smallest)
def  main():
  while True:
    n=myinput()
    if num == "done": 
      break    
    l=large(n)
    s=small(n)
    output(l,s)
main()    