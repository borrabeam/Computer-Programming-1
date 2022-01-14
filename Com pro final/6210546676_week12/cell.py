

class Cell:

    def __init__(self,id,move,hold):
        self.__cell_id = id
        self.__move = move
        self.__hold = hold
        self.__occupy_list = []

    def get_occupy_list(self):
        space = ''
        for player in self.__occupy_list:
            space += player.get_name() + ','
        return space   

    def add_occupy_list(self,x):
        return  self.__occupy_list.append(x)
    
    def remove_occupy_list(self,x):
      return  self.__occupy_list.remove(x)

      
    @property
    def occupy_list(self):
        return self.__occupy_list

    def __str__(self):
        return f'{self.__cell_id},{self.__move},{self.__hold}'

