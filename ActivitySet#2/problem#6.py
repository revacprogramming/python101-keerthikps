class Menu:
  cost=0
  name=""
  def add(self,n,c):
    self.name=n
    self.cost=c
    
  def show(self):
    print(self.name," costs ",self.cost)

m = Menu()  # Menu is a class
m.add("idly", 10)
m.show()
m.add("vada", 20)
m.show()
