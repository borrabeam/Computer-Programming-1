class Item:
    def __init__(self,id_c,type_c,color):
        self.__id = id_c
        self.__type_c = type_c
        self.__color = color
    
    def __eq__(self,id):
        if self.__id == id:
            return True
        else:
            return False

    def __str__(self):
        return '{0},{1},{2}'.format(self.__id,self.__type_c,self.__color)




    # @property
    # def id(self):
    #     return self.__id
    # @id.setter
    # def id(self,num):
    #     self.__id = num


    # @property
    # def type_c(self):
    #     return self.__type_c
    # @type_c.setter
    # def type_c(self,cloth):
    #     self.__type_c = cloth

    
    # @property
    # def color(self):
    #     return self.__color
    # @color.setter
    # def color(self,color):
    #     self.__color = color

