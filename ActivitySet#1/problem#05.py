# Functions
def computepay(h,r):
    if h > 40:
        p = 1.5 * r * (h - 40) + (40 *r)
    else:
        p = h * r
    return p
def output(p):
  	print("Pay",p)
def main():
  hrs = input("Enter Hours:")
  hr = float(hrs)
  rphrs = input("Enter rate per hour:")
  rphr = float(rphrs)
  p = computepay(hr,rphr)
  output(p)
main()