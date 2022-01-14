from item import *
from stock import *
from order import *

item1 = Item(1,'T-shirt', 'White')
item2 = Item(2,'T-shirt', 'Black')
item3 = Item(3,'Polo-shirt', 'White')
item4 = Item(4,'Polo-shirt', 'Green')
item5 = Item(5,'Shirt', 'Green')
item6 = Item(6,'Shirt', 'Black')
print(item1)
print(item2)


print(item1 == item2)
print(item2 == item2)


stock1 = Stock(item1, 100, 60)
stock2 = Stock(item2, 100, 90)
stock3 = Stock(item3, 100, 120)
stock4 = Stock(item4, 100, 140)
stock5 = Stock(item5, 100, 200)
stock6 = Stock(item6, 100, 220)
print(stock3)
print(stock5)


order1 = Order(item1, 10)
print(order1)


stock_list = []
def print_stock_list(stock_list): 
        print("Stock List:")    
        print(stock1)
        print(stock2)
        print(stock3)
        print(stock4)
        print(stock5)
        print(stock6)



print_stock_list(stock_list)

item_list = []
def print_item_list(item_list):
    print("Item List:")
    print(item1)
    print(item2)
    print(item3)
    print(item4)
    print(item5)
    print(item6)

print_item_list(item_list)