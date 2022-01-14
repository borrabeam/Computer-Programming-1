from cell import *

class Board:
    def __init__(self,filename,length = 0,width= 0):
        # self.__board_file = self.read_board(filename)
        self.cell_list: Cell = []
        self.length = length
        self.width = width
        self.read_board(filename)

    def read_board(self, filename):
        list1 = []
        lines = open(filename).read().splitlines()
        
        # for i in lines:

        for x in lines:
            x = x.split(",")
            
            list1.append(x)
        
        for i in list1:
            if len(i) > 1:

                self.cell_list.append(Cell(i[0],i[1],i[2]))

        self.width = list1[0][0]
        self.length = list1[1][0]

        
    def __str__(self):
        space = ''
        for i in self.cell_list:
            space += i.__str__() + "\n"
        return space

        