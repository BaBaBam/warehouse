from numpy import *
import pandas as pd
class Conveyor:
   def __init__(self):
       self.in_belt = []
       self.item_in_line = 0
   def retrieveProduct(self, id_product):
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
           r.rehash_key[self.in_belt[0]] = "    "
           del self.in_belt[0]
           self.item_in_line -= 1
           print("The belt now has "+str(self.item_in_line)+" products on the line")
   def getItem(self):
       return self.item_in_line
class Warehouse:
   def __init__(self, names, rows, grids):
       """defualt name warehouse"""
       self.name = names
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
           self.rows[i] = pd.DataFrame(data=data_slot, columns=[y for y in range(self.grids)], index=[x for x in range(self.grids)])
       # """Recheck Here!!! all of # below here"""
       # print("__________________________________________________")
       # for i in range(self.num_rows):
       #     print("rows : "+str(i+1))
       #     print(self.rows[i])
       #     print("__________________________________________________")
       print("Create Warehouse "+self.name+" Successfully")
       # print("---------------------------------------------------------------------------")
       # print("---------------------------------------------------------------------------")
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
       self.list_product[row].remove(id_product)
       self.rows[row][y][x] = "    "
       self.total_product -= 1
   def sortRow(self, row):
       self.list_product[row].sort()
       return self.list_product[row]
   def stateData(self):
       print("Warehouse " + self.name)
       print("Number of Rows : " + str(self.num_rows))
       print("Numbers of total product : " + str(self.total_product))
       for i in range(self.num_rows):
           string = " "
           if len(self.list_product[i]) > 0:
               for item in (self.list_product[i]):
                   string = string + str(item) + ", "
               print("Product in row " + str(i + 1) + " : id" + string[0:-2])
           else:
               print("Product in row " + str(i + 1) + " : id -")
       print("__________________________________________________")
       for i in range(self.num_rows):
           print("rows : "+str(i+1))
           print(self.rows[i])
           print("__________________________________________________")
       print("---------------------------------------------------------------------------")
       print("---------------------------------------------------------------------------")
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
def showdataAll():
   wh1.stateData()
   wh2.stateData()
   wh3.stateData()
   wh4.stateData()
   wh5.stateData()
def getInfoAll():return wh1.getInfo(), wh2.getInfo(), wh3.getInfo(), wh4.getInfo(), wh5.getInfo()
class Robot:
   def __init__(self):
       self.list_wh = [wh1, wh2, wh3, wh4, wh5]
       self.rehash_key = {}
       self.hash_warehouse = 0
       self.hash_row = 0
       self.hash_slot = 0
       for i in "ABCDEFGHIJKLMNOPQRSTUVWXY":
           for j in "12345":
               for k in "0123456789":
                   for l in "0123456789":
                       id_product = i+j+k+l
                       self.rehash_key[id_product] = "    "
       self.id_product = "    "
   def findProduct(self, product_id):
       if (self.rehash_key[product_id] != "    ") and (self.rehash_key[product_id] != "Belt"):
               print("Found the product at " + self.rehash_key[product_id])
       else:
           print("Product not found")
   def hashing_key(self, id_product):
       self.id_product = id_product
       """transform product_id in charactor to number_code"""
       if ord(id_product[0]) % 2 == 0:
           position = int(ord(id_product[0]) / 2) * 1000 + int(id_product[1:])
       else:
           position = int(ord(id_product[0]) / 2) * 1000 + 500 + int(id_product[1:])
           ##########################################################################################################
       """hashing id product for store in the warehouse"""
       if (position >= 32600) and (position < 33100):
           self.hash_warehouse = 1
           self.hash_row = int(position / 100) - 326
           self.hash_slot = (position - 32600) % 100
       elif (position >= 33100) and (position < 33600):
           self.hash_warehouse = 2
           self.hash_row = int(position / 100) - 331
           self.hash_slot = (position - 33100) % 100
       elif (position >= 33600) and (position < 34100):
           self.hash_warehouse = 3
           self.hash_row = int(position / 100) - 336
           self.hash_slot = (position - 33600) % 100
       elif (position >= 34100) and (position < 34600):
           self.hash_warehouse = 4
           self.hash_row = int((position - 34100) / 25) % 7
           self.hash_slot = int((position - 34100) % 25)
       else:
           self.hash_warehouse = 5
           self.hash_row = int((position - 34600) / 400) % 20
           self.hash_slot = int((position - 34600) % 400)
   def retrieve(self,id_product):
       if belt.getItem() == 10:
           return print("Belt is full. Cannot retrieve the product")
       if self.rehash_key[id_product] == "    ":
           return print("Slot is empty. Cannot retrieve the product")
       if self.rehash_key[id_product] == "Belt":
           return print("now product " + id_product + " is on belt. Cannot retrieve the product")
       else:
           self.id_product = id_product
           self.hashing_key(self.rehash_key[self.id_product])
           print("Moving from Belt to A")
           self.list_wh[self.hash_warehouse-1].removeProduct(id_product, self.hash_row, self.hash_slot)
           if self.hash_warehouse == 1:
               print("Getting a product id " + id_product + " in warehouse A : row " + str(self.hash_row + 1) + " slot " + str(self.hash_slot))
           elif self.hash_warehouse == 2:
               print("Moving from A to B  ")
               print("Getting a product id " + id_product + " in warehouse B : row " + str(self.hash_row + 1) + " slot " + str(self.hash_slot))
               print("Moving from B to A  ")
           elif self.hash_warehouse == 3:
               print("Moving from A to C  ")
               print("Getting a product id " + id_product + " in warehouse C : row " + str(self.hash_row + 1) + " slot " + str(self.hash_slot))
               print("Moving from C to A  ")
           elif self.hash_warehouse == 4:
               print("Moving from A to B\nMoving from B to D  ")
               print("Getting a product id " + id_product + " in warehouse D : row " + str(self.hash_row + 1) + " slot " + str(self.hash_slot))
               print("Moving from D to B\nMoving from B to A  ")
           elif self.hash_warehouse == 5:
               print("Moving from A to B\nMoving from B to E  ")
               print("Getting a product id " + id_product + " in warehouse E : row " + str(self.hash_row + 1) + " slot " + str(self.hash_slot))
               print("Moving from E to B\nMoving from B to A  ")
           self.rehash_key[id_product] = "Belt"
           print("Moving from A to Start ")
           belt.retrieveProduct(product_id1)
   def store(self, id_product):
       self.hashing_key(id_product)
       warehouse = self.hash_warehouse
       row = self.hash_row
       slot = self.hash_slot
       if self.rehash_key[id_product] == "Belt":
           return print("now product " + id_product + " is on belt. Cannot store the product. ")
       if self.rehash_key[id_product] != "    ":
           return print("product has been stored. Cannot store the product.")
       self.list_wh[warehouse-1].checkSlot(row, slot)
       if self.list_wh[warehouse-1].checkSlot(row, slot) != "    ":
           return print("Slot is occupied. Cannot store the product. ")
       else:
           print("Moving from Belt to A")
           self.list_wh[warehouse - 1].addProduct(id_product, row, slot)
           if warehouse == 1:
               print("Storing a product id " + id_product + " in warehouse A : row " + str(row + 1) + " slot " + str(slot))
           elif warehouse == 2:
               print("Moving from A to B  ")
               print("Storing a product id " + id_product + " in warehouse B : row " + str(row + 1) + " slot " + str(slot))
               print("Moving from B to A  ")
           elif warehouse == 3:
               print("Moving from A to C  ")
               print("Storing a product id " + id_product + " in warehouse C : row " + str(row + 1) + " slot " + str(slot))
               print("Moving from C to A  ")
           elif warehouse == 4:
               print("Moving from A to B\nMoving from B to D  ")
               print("Storing a product id " + id_product + " in warehouse D : row " + str(row + 1) + " slot " + str(slot))
               print("Moving from D to B\nMoving from B to A  ")
           elif warehouse == 5:
               print("Moving from A to B\nMoving from B to E  ")
               print("Storing a product id " + id_product + " in warehouse E : row " + str(row + 1) + " slot " + str(slot))
               print("Moving from E to B\nMoving from B to A  ")
           print("Moving from A to Start ")
           self.rehash_key[id_product] = id_product
           print("Storing Successfully!")
   def manuallmove(self, id_product1, id_product2):
       self.hashing_key(id_product2)
       if self.list_wh[self.hash_warehouse - 1].checkSlot(self.hash_row, self.hash_slot) != "    ":
           return print("Slot is occupied. Cannot move the product. ")
       if self.rehash_key[id_product1] == "Belt":
           return print("now product " + id_product1 + " is on belt. Cannot move the product.")
       if self.rehash_key[id_product1] == "    ":
           return print("Slot is empty. Cannot move the product")
       if self.rehash_key[id_product1] != "    ":
           self.hashing_key(self.rehash_key[id_product1])
           self.list_wh[self.hash_warehouse - 1].removeProduct(id_product1, self.hash_row, self.hash_slot)
           self.hashing_key(id_product2)
           self.list_wh[self.hash_warehouse - 1].addProduct(id_product1, self.hash_row, self.hash_slot)
           self.rehash_key[id_product1] = id_product2
           return print("Move product " + id_product1 + " to " + id_product2)
   def sortWarehouse(self, sort_warehouse, rows):
       rows = rows - 1
       product_move = []
       product_row = self.list_wh[sort_warehouse-1].sortRow(rows)
       for item in range(0, len(product_row)):
           if self.rehash_key[product_row[item]] != product_row[item]:
               product_move.append(product_row[item])
               self.hashing_key(product_row[item])
               if self.list_wh[self.hash_warehouse - 1].checkSlot(self.hash_row, self.hash_slot) != "    ":
                   return print("Slot is occupied. Fail to sort. ")
       if len(product_move) != 0:
           for item in range(0, len(product_move)):
               self.hashing_key(self.rehash_key[product_move[item]])
               self.list_wh[self.hash_warehouse - 1].removeProduct(product_move[item], self.hash_row, self.hash_slot)
               self.hashing_key(product_move[item])
               self.list_wh[self.hash_warehouse - 1].addProduct(product_move[item], self.hash_row, self.hash_slot)
               self.rehash_key[product_move[item]] = product_move[item]
       print("Sorting process for warehouse "+self.list_wh[sort_warehouse-1].name+" is complete")
"""INPUT COMMAND"""
input_command = ""
r = Robot()
while(input_command != "stop"):
   print("0XXXX\t\tRetrieve a product id XXXX ")
   print("1XXXX\t\tStore a product id XXXX ")
   print("2XYY0\t\tSort warehouse X at row Y ")
   print("30000\t\tRetrieve a product from the conveyor belt ")
   print("40000\t\tOutput information of all warehouses")
   print("5XXXX\t\tSearch for a product ID XXXX ")
   print("60000\t\tshow all id_product and position_id")
   print("70000\t\tshow inside of all warehouse")
   print("9XXXXYYYY\tManually put a product id XXXX at position YYYY")
   print("stop\t\tstop program")
   print("-----------------------------------------------------------------------------------------")
   input_command = input("Input Command : ")
   if input_command != "stop":
       if (len(input_command) == 5) or (len(input_command) == 9):
           order = input_command[0]
           product_id1 = input_command[1:5]
           product_id2 = input_command[5:9]
           if ord(product_id1[0]) > 96 & ord(product_id1[0]) < 122:
               product_id1 = product_id1[0].upper() + input_command[2:5]
           if len(input_command) == 9:
               if ord(product_id2[0]) > 96 & ord(product_id2[0]) < 122:
                   product_id2 = product_id2[0].upper() + input_command[6:9]
           if input_command == str('30000'):belt.getProduct()
           if input_command == str('40000'):getInfoAll()
           if input_command == str('60000'):print(r.rehash_key)
           if input_command == str('70000'):showdataAll()
           if order == str('0'):r.retrieve(product_id1)
           if order == str('1'):r.store(product_id1)
           if order == str('2'):r.sortWarehouse(ord(input_command[1].upper()) - 64, int(input_command[2:4]))
           if order == str('5'):r.findProduct(product_id1)
           if order == str('9'):r.manuallmove(product_id1, product_id2)
       else:
           print("your order is not clear please input again")