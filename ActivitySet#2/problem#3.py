def get_cs():
   string=input("Enter a string: ")
   return string

def cs_to_lot(cs):
   lot=cs.split()
   return lot

def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)

_name_=input("Enter the name: ")
if _name_ == '_main_':
    main()
