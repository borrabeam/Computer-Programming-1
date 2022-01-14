class Football:
    def __init__(self,short_name,full_name,wins=0,draws=0,loses=0):
        self.__full_name = full_name
        self.__short_name = short_name
        self.__wins = wins
        self.__draws = draws
        self.__loses = loses

    def __str__(self):
        return '#{0},{1},{2},{3},{4}'.format(self.__full_name,self.__short_name,self.__wins,self.__draws,self.__loses)
    
    @property
    def full_name(self):
        return self.__full_name
    @full_name.setter
    def full_name(self,name):
        self.__full_name = name

    @property
    def short_name(self):
        return self.__short_name
    @short_name.setter
    def short_name(self,name):
        self.__short_name = name
    
    @property
    def win(self):
        return self.__wins
    @win.setter
    def win(self,num):
        self.__wins = num
    
    @property
    def draw(self):
        return self.__draws
    @draw.setter
    def draw(self,num):
        self.__draws = num

    @property
    def lose(self):
        return self.__loses
    @lose.setter
    def lose(self,num):
        self.__loses = num

    @property  
    def won(self):
        return self.__wins
    @won.setter
    def won(self,name):
        self.__wins(name)
    # def won(self,team):
    #     self.team.won() += 1
       
    


    
# def won(team1,team2):
#     if team1 == team1.won:
#         # self.__wins += 1
#         # team2.lose += 1
#     # elif team2 == team2.win:
#     #     team2.win += 1
#     #     team1.lose += 1
    
        

        

        