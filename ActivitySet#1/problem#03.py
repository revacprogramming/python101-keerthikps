# Variables, Expressions & Statements
def compute(hrs,rate):
  earn=hrs*rate
  return earn
def output(earn):
  print(earn)
def main():
  hrs = float(input("Enter hours? "))
  rate=float(input("enter Rate :"))
  earn=compute(hrs,rate)
  output(earn)
main()