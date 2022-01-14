class Player:
    def __init__(self,name,pos=0,hold=False,move=0):
        self.__name = name
        self.__pos = pos
        self.__hold = hold
        self.__move = move

    def __str__(self):
        
        return '{0}: Pos = {1}: Hold = {1}: Move = {2}'.format(self.__name,self.__pos,self.__hold,self.__move)