from item import *

class Stock:
    def __init__(self,item,amount,price):
        self.__item = item
        self.__amount = amount
        self.__price = price

    def __str__(self):
        return '{0},{1},{2}'.format(self.__item,self.__amount,self.__price)
    

