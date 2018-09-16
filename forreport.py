from numpy import *
import pandas as pd
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
class Warehouse:
   def __init__(self, name, rows, grids):
       """defualt name warehouse"""
       self.name = name
       """defualt parameter  name  row  grid"""
       self.num_rows = rows
       """what warehouse name is How many row and grid"""
       self.grids = grids
       self.rows = []
       self.total_product = 0
       self.list_slot = []
       self.slot = 0
       """defualt position x,y"""
       self.x = 0
       self.y = 0
       self.list_product = []
   def createWarehouse(self):
       """Create Warehouse with data from"""
       print("Create Warehouse "+self.name)
       print("Number of Rows : "+str(self.num_rows))
       print("Warehouse is Building")
       """create grids for each row"""
       ###################################################################################
       """create row"""
       for r in range(self.num_rows):
           self.rows.append([])
           """create parameter to store id product that is stored in that row"""
           self.list_product.append([])
       for num in range(0, (self.grids*self.grids)):                     #build grid x grid
           self.list_slot.append("    ")                              #position x,y in grid we call slot
       data_slot = array(self.list_slot).reshape(self.grids, self.grids)
       ###################################################################################
       for i in range(self.num_rows):                                 #take grid 2 dimension into rows of that warehouse
           self.rows[i] = pd.DataFrame(data = data_slot, columns=[y for y in range(self.grids)], index=[x for x in range(self.grids)])
       """Recheck Here!!! all of # below here"""
#         print("__________________________________________________")
#         for i in range(self.num_rows):
#             print("rows : "+str(i+1))
#             print(self.rows[i])
#             print("__________________________________________________")
       print("Create Warehouse "+self.name+" Successfully")
#         print("---------------------------------------------------------------------------")
#         print("---------------------------------------------------------------------------")
   def getInfo(self):                                                  #show Information about warehouse
       print("Warehouse "+self.name)
       print("Number of Rows : "+str(self.num_rows))
       print("Numbers of total product : "+str(self.total_product))
       for i in range(self.num_rows):
           string = " "
           if len(self.list_product[i])>0:
               for item in (self.list_product[i]):
                   string = string+str(item)+", "
               print("Product in row "+str(i+1)+" : id"+string[0:-2])
           else:
               print("Product in row "+str(i+1)+" : id -")
   def checkSlot(self,row,slot):                                         #check Dose it has id_product in slot right?
       x = int(slot / self.grids)
       y = int(slot % self.grids)
       return self.rows[row][y][x]
   def addProduct(self,id_product,row,slot):                           #store product into warehouse
       x = int(slot / self.grids)
       y = int(slot % self.grids)
       self.rows[row][y][x] = id_product
       self.list_product[row].append(id_product)
       self.total_product += 1
   def removeProduct(self, id_product, row, slot):                         #retrieve product from warehouse
       x = int(slot / self.grids)
       y = int(slot % self.grids)
       # if self.rows[row][y][x] != "    ":
       self.list_product[row].remove(id_product)
       self.rows[row][y][x] = "    "
       self.total_product -= 1
   def replaceProduct(self, id_product, row, slot):  # store product into warehouse
       x = int(slot / self.grids)
       y = int(slot % self.grids)
       self.rows[row][y][x] = id_product
   def sortRow(self,row):
       self.list_product[row].sort()
       return self.list_product[row]
rehash_key = {}
for i in "ABCDEFGHIJKLMNOPQRSTUVWXY":
   for j in "12345":
       for k in "0123456789":
           for l in "0123456789":
               id_product = i+j+k+l
               rehash_key[id_product] = "    "
belt = Conveyor()
wh1 = Warehouse('A', 5, 10)
wh1.createWarehouse()
wh2 = Warehouse('B', 5, 10)
wh2.createWarehouse()
wh3 = Warehouse('C', 5, 10)
wh3.createWarehouse()
wh4 = Warehouse('D', 7, 5)
wh4.createWarehouse()
wh5 = Warehouse('E', 20, 20)
wh5.createWarehouse()
warehouse = 0
row = 0
slot = 0
def getInfo():
   return wh1.getInfo(), wh2.getInfo(), wh3.getInfo(), wh4.getInfo(), wh5.getInfo()
def hashing_key(id_product):
   """transform product_id in charactor to number_code"""
                                             #for store id_product by dont set the position it will be hashed
   if ord(id_product[0]) % 2 == 0:
       position = int(ord(id_product[0])/2)*1000+int(id_product[1:])
   else:
       position = int(ord(id_product[0])/2)*1000+500+int(id_product[1:])
##########################################################################################################
   """hashing id product for store in the warehouse"""
   if position < 33100:
       hash_warehouse = 1
       hash_row = int(position/100)-326
       hash_slot = (position-32600) % 100

   elif (position >= 33100) and (position < 33600):
       hash_warehouse = 2
       hash_row = int(position/100)-331
       hash_slot = (position-33100) % 100

   elif (position >= 33600) and (position < 34100):
       hash_warehouse = 3
       hash_row = int(position/100)-336
       hash_slot = (position-33600) % 100
   elif (position >= 34100) and (position < 34600):
       hash_warehouse = 4
       hash_row = int((position-34600)/25) % 7
       hash_slot = int((position-34600) % 25)
   else:
       hash_warehouse = 5
       hash_row = int((position-35100)/400) % 20
       hash_slot = int((position-35100) % 400)
   return[hash_warehouse, hash_row, hash_slot]
def retrieve(id_product):
   if rehash_key[id_product] == "    ":
       return print("Slot is empty. Cannot retrieve the product")
   else:
       position_point = hashing_key(rehash_key[id_product])
       re_warehouse = position_point[0]
       re_row = position_point[1]
       re_slot =  position_point[2]
       print("Moving from Belt to A")
       if re_warehouse == 1:
           wh1.removeProduct(id_product, re_row, re_slot)
           print("Getting a product id "+id_product+" in warehouse A : row "+str(re_row + 1)+" slot "+str(re_slot))
       elif re_warehouse == 2:
           print("Moving from A to B  ")
           wh2.removeProduct(id_product, re_row, re_slot)
           print("Getting a product id "+id_product+" in warehouse B : row "+str(re_row + 1)+" slot "+str(re_slot))
           print("Moving from B to A  ")
       elif re_warehouse == 3:
           print("Moving from A to C  ")
           wh3.removeProduct(id_product, re_row, re_slot)
           print("Getting a product id "+id_product+" in warehouse C : row "+str(re_row + 1)+" slot " + str(re_slot))
           print("Moving from C to A  ")
       elif re_warehouse == 4:
           print("Moving from A to B  ")
           print("Moving from B to D  ")
           wh4.removeProduct(id_product, re_row, re_slot)
           print("Getting a product id "+id_product+" in warehouse D : row "+str(re_row + 1)+" slot "+str(re_slot))
           print("Moving from D to B  ")
           print("Moving from B to A  ")
       elif re_warehouse == 5:
           print("Moving from A to B  ")
           print("Moving from B to E  ")
           wh5.removeProduct(id_product, re_row, re_slot)
           print("Getting a product id "+id_product+" in warehouse E : row "+str(re_row + 1)+" slot "+str(re_slot))
           print("Moving from E to B  ")
           print("Moving from B to A  ")
       rehash_key[id_product] = "    "
       print("Moving from A to Start ")
       belt.retrieve(id_product)
def store(id_product):
   position_point = hashing_key(id_product)
   warehouse = position_point[0]
   row = position_point[1]
   slot = position_point[2]
   if rehash_key[id_product] != "    ":
       return print("product has been stored")
   check_slot = "    "
   if warehouse == 1:
       check_slot = wh1.checkSlot(row, slot)
   if warehouse == 2:
       check_slot = wh2.checkSlot(row, slot)
   if warehouse == 3:
       check_slot = wh3.checkSlot(row, slot)
   if warehouse == 4:
       check_slot = wh4.checkSlot(row, slot)
   if warehouse == 5:
       check_slot = wh5.checkSlot(row, slot)
   if check_slot != "    ":
       return print("Slot is occupied. Cannot store the product. ")
   else:
       # position_point = hashing_key(id_product)
       # warehouse = position_point[0]
       # row = position_point[1]
       # slot = position_point[2]
       print("Moving from Belt to A")
       if warehouse == 1:
           wh1.addProduct(id_product, row, slot)
           print("Storing a product id " + id_product + " in warehouse A : row " + str(row + 1) + " slot " + str(slot))
       elif warehouse == 2:
           print("Moving from A to B  ")
           wh2.addProduct(id_product, row, slot)
           print("Storing a product id " + id_product + " in warehouse B : row " + str(row + 1) + " slot " + str(slot))
           print("Moving from B to A  ")
       elif warehouse == 3:
           print("Moving from A to C  ")
           wh3.addProduct(id_product, row, slot)
           print("Storing a product id " + id_product + " in warehouse C : row " + str(row + 1) + " slot " + str(slot))
           print("Moving from C to A  ")
       elif warehouse == 4:
           print("Moving from A to B  ")
           print("Moving from B to D  ")
           wh4.addProduct(id_product, row, slot)
           print("Storing a product id " + id_product + " in warehouse D : row " + str(row + 1) + " slot " + str(slot))
           print("Moving from D to B  ")
           print("Moving from B to A  ")
       elif warehouse == 5:
           print("Moving from A to B  ")
           print("Moving from B to D  ")
           wh5.addProduct(id_product, row, slot)
           print("Storing a product id " + id_product + " in warehouse E : row " + str(row + 1) + " slot " + str(slot))
           print("Moving from E to B  ")
           print("Moving from B to A  ")
       print("Moving from A to Start ")
       rehash_key[id_product] = id_product
       print("Storing Successfully!")
def manuallmove(id_product1, id_product2):
   if rehash_key[id_product2] != "    ":
       return print("Slot is occupied. Failed to move. ")
   if rehash_key[id_product1] != "    ":
       hashing_key(rehash_key[id_product1])
       position_point = hashing_key(id_product1)
       warehouse = position_point[0]
       row = position_point[1]
       slot = position_point[2]
       if warehouse == 1:
           wh1.removeProduct(id_product1, row, slot)
       elif warehouse == 2:
           wh2.removeProduct(id_product1, row, slot)
       elif warehouse == 3:
           wh3.removeProduct(id_product1, row, slot)
       elif warehouse == 4:
           wh4.removeProduct(id_product1, row, slot)
       elif warehouse == 5:
           wh5.removeProduct(id_product1, row, slot)
   if rehash_key[id_product1] == "    ":
       hashing_key(id_product2)
       position_point = hashing_key(id_product2)
       warehouse = position_point[0]
       row = position_point[1]
       slot = position_point[2]
       if warehouse == 1:
           wh1.addProduct(id_product1, row, slot)
       elif warehouse == 2:
           wh2.addProduct(id_product1, row, slot)
       elif warehouse == 3:
           wh3.addProduct(id_product1, row, slot)
       elif warehouse == 4:
           wh4.addProduct(id_product1, row, slot)
       elif warehouse == 5:
           wh5.addProduct(id_product1, row, slot)
       rehash_key[id_product1] = id_product2
       return print("Move product "+id_product1+" to "+id_product2)
def sortWarehouse(sort_warehouse, rows):
   rows = rows-1
   product_row = []
   product_move = []
   if sort_warehouse == 1:
       product_row = wh1.sortRow(rows)
   if sort_warehouse == 2:
       product_row = wh2.sortRow(rows)
   if sort_warehouse == 3:
       product_row = wh3.sortRow(rows)
   if sort_warehouse == 4:
       product_row = wh4.sortRow(rows)
   if sort_warehouse == 5:
       product_row = wh5.sortRow(rows)
   for item in range(0, len(product_row)):
       if rehash_key[product_row[item]] != product_row[item]:
           product_move.append(product_row[item])
           position_point = hashing_key(product_row[item])
           warehouse = position_point[0]
           rows = position_point[1]
           slots = position_point[2]
           if warehouse == 1:
               if wh1.checkSlot(rows,slots) != "    ":
                   return print("Slot is occupied.Fail to sort")
           elif warehouse == 2:
               if wh2.checkSlot(rows, slots) != "    ":
                   return print("Slot is occupied.Fail to sort")
           elif warehouse == 3:
               if wh3.checkSlot(rows, slots) != "    ":
                   return print("Slot is occupied.Fail to sort")
           elif warehouse == 4:
               if wh4.checkSlot(rows, slots) != "    ":
                   return print("Slot is occupied.Fail to sort")
           elif warehouse == 5:
               if wh5.checkSlot(rows, slots) != "    ":
                   return print("Slot is occupied.Fail to sort")
   if len(product_move) != 0:
       for item in range(len(product_move)):
           position_point = hashing_key(rehash_key[product_move[item]])
           warehouse = position_point[0]
           row = position_point[1]
           slot = position_point[2]
           if warehouse == 1:
               wh1.removeProduct(product_move[item], row, slot)
           elif warehouse == 2:
               wh2.removeProduct(product_move[item], row, slot)
           elif warehouse == 3:
               wh3.removeProduct(product_move[item], row, slot)
           elif warehouse == 4:
               wh4.removeProduct(product_move[item], row, slot)
           elif warehouse == 5:
               wh5.removeProduct(product_move[item], row, slot)
           hashing_key(product_move[item])
           position_point = hashing_key(product_move[item])
           warehouse = position_point[0]
           row = position_point[1]
           slot = position_point[2]
           if warehouse == 1:
               wh1.addProduct(product_move[item], row, slot)
           elif warehouse == 2:
               wh2.addProduct(product_move[item], row, slot)
           elif warehouse == 3:
               wh3.addProduct(product_move[item], row, slot)
           elif warehouse == 4:
               wh4.addProduct(product_move[item], row, slot)
           elif warehouse == 5:
               wh5.addProduct(product_move[item], row, slot)
           rehash_key[product_move[item]] = product_move[item]
   if sort_warehouse == 1:
       print("Sorting process for warehouse A is complete")
   if sort_warehouse == 2:
       print("Sorting process for warehouse B is complete")
   if sort_warehouse == 3:
       print("Sorting process for warehouse C is complete")
   if sort_warehouse == 4:
       print("Sorting process for warehouse D is complete")
   if sort_warehouse == 5:
       print("Sorting process for warehouse E is complete")
"""INPUT COMMAND"""
input_command = ""
while(input_command != "stop"):
   print("0XXXX\t\tRetrieve a product id XXXX ")
   print("1XXXX\t\tStore a product id XXXX ")
   print("2XY00\t\tSort warehouse X at row Y ")
   print("30000\t\tRetrieve a product from the conveyor belt ")
   print("40000\t\tOutput information of all warehouses")
   print("5XXXX\t\tSearch for a product ID XXXX ")
   print("9XXXXYYYY\tManually put a product id XXXX at position YYYY")
   print("-----------------------------------------------------------------------------------------")
   input_command = input("Input Command : ")
   if input_command != "stop":
       order = input_command[0]
       product_id1 = input_command[1:5]
       product_id2 = input_command[5:9]
       if ord(product_id1[0]) > 90:
           product_id1 = product_id1[0].upper() + input_command[2:5]
       if len(input_command) > 5:
           if ord(product_id2[0]) > 90:
               product_id2 = product_id2[0].upper() + input_command[6:9]
       if order == str('0'):
           retrieve(product_id1)
       elif order == str('1'):
           store(product_id1)
       elif order == str('2'):
           sortWarehouse(ord(input_command[1].upper()) - 64, int(input_command[2:4]))
       elif input_command == str('30000'):
           belt.getProduct()
       elif input_command == str('40000'):
           getInfo()
       elif order == str('5'):
           if rehash_key[product_id1] != "    ":
               print("Found the product at " + rehash_key[product_id1])
           else:
               print("Product not found")
       elif input_command == str('60000'):
           print(rehash_key)
       elif order == str('9'):
           manuallmove(product_id1, product_id2)

