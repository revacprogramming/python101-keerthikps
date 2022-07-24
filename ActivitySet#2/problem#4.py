def get_cs():
  string=input("Enter a string: ")
  return string

def cs_to_lot(cs):
  lst=cs.split()
  return lst

def lot_to_cs(lot):
  string=""
  for i in lot:
    string=string+i
  return string

def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)

_name_=input("enter the name: ")
if _name_ == '_main_':
    main()
