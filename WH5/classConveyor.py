class Conveyor:
   def __init__(self):
       self.in_belt = []
       self.item_in_line = 0
   def retrieve(self, id_product):
       if self.item_in_line == 10:
           print("Belt is full. Cannot retrieve the product")
       else:
           self.in_belt.append(id_product)
           print("Place product id "+id_product+" on the belt")
           self.item_in_line += 1
           print("Retrieving Successfully!  ")
           return self.in_belt
   def getProduct(self):
       if self.item_in_line == 0:
           print("The belt is empty. Cannot retrieve the product from the belt. ")
       else:
           print("Retrieve a product with id "+self.in_belt[0]+" from the belt")
           del self.in_belt[0]
           self.item_in_line -= 1
           print("The belt now has "+str(self.item_in_line)+" products on the line")
   def getItem(self):
       return self.item_in_line