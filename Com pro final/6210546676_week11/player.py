import random


class Player:
    
    def __init__(self,name= 'None',num_win = 0,num_play = 0, hand = 'None'):
        self.__name = name
        self.__num_wins = num_win
        self.__num_plays = num_play
        self.__hand = hand

    def __str__(self):
        return '{0}: Wins = {1}: Plays = {2}:Hand = {3}'.format(self.__name,self.__num_wins,self.__num_plays,self.__hand)
    
    def get_name(self):
        return self.__name

    def set_name(self,value):
        self.__name = value
    
    def get_num_wins(self):
        return self.__num_wins
    
    def set_num_wins(self,value):
        self.__num_wins = value

    def get_num_plays(self):
        return self.__num_plays
    
    def set_num_plays(self,value):
        self.__num_plays = value

    def get_hand(self):
        return self.__hand

    def set_hand(self, value):
        self.__hand = value
        
    # @property
    # def num_plays(self):
    #     return self.__num_plays

    # @num_plays.setter
    # def num_plays(self,value):
    #     self.__num_plays = value

    # @property
    # def num_wins(self):
    #     return self.__num_wins

    # @num_wins.setter
    # def num_wins(self,value):
    #     self.__num_wins = value

    # @property
    # def hand(self):
    #     return self.__hand
    # @hand.setter
    # def hand(self,value):
    #     self.__hand = value

    def randomize_hand(self):
        x = random.randint(1,3)
        if x == 1:
            self.__hand = 'Rock'
        elif x == 2:
            self.__hand = 'Paper'
        elif x == 3:
            self.__hand = 'Scissors'

    
