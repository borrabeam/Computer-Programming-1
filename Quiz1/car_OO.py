class Car:

    def __init__(self,brand = '_',model = '_',price = 0):
        self.__brand = brand
        self.__model = model
        self.__price = price

    def __str__(self):
        return 'Brand: {0}, Model: {1}, Price: {2}'.format(self.__brand,self.__model,self.__price)

    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self,name):
        self.__brand = name

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self,name):
        self.__model = name

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,name):
        self.__price = name




def compare(car1,car2):
    print(car1)
    print(car2)


    