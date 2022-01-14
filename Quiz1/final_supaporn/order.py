from item import *

class Order:
    def __init__(self,item,amount,cost=0,status = "To process"):
        self.__item = item
        self.__status = status
        self.__amount = amount
        self.__cost = cost

    def __str__(self):
        return '{0},{1},{2} Baht,{3}'.format(self.__item,self.__amount,self.__cost,self.__status)

