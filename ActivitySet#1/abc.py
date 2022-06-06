def f(*args,**kar gs):
  print(args,*args,kargs) #**kargs)  
f(1,2,3,a=10,b=20)  

def comparision():
    largest = None
    smallest = None
    while True:
        num = input("Enter a number: ")
        if num == "done": 
            break
        try:
            num = int(num)
            if largest is None or largest < num:
                largest = num
            if smallest is None or smallest > num: 
                smallest = num
        except:
            print ("Invalid input")
    return largest,smallest
def output(largest,smallest):
  print ("Maximum is",largest)
  print ("Minimum is",smallest)
def main():
  largest,smallest=comparision() 
  output(largest,smallest)
main()