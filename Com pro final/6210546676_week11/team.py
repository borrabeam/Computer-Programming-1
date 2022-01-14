import random
from player import *

class Team:
    def __init__(self, filename, team_name='No Name'):
        self.__player_list = self.__read_team(filename)
        self.__current_player = self.__player_list[0]
        self.team_name = team_name
        self.team_point = 0 

    def __read_team(self, filename):
        player_list = []
        lines = open(filename).read().splitlines()
        for x in lines:
            x = x.split(",")
            name = x[0]
            num_win = x[1]
            num_play = x[2]
            player_list.append(Player(name, num_win, num_play))r
        return player_list

    def select_player(self):
        self.__current_player = self.__player_list[random.randint(0,len(self.__player_list)-1)]
        self.__current_player.randomize_hand()

    def update_team_points(self, value):
        if value == 'win':
            self.team_point +=1
            self.current_player.set_num_wins(int(self.current_player.get_num_wins()) + 1)
        self.current_player.set_num_plays(int(self.current_player.get_num_plays()) + 1)
        # else:
        #     self.current_player.set_num_plays(int(self.current_player.get_num_plays()) + 1)


    @property
    def current_player(self):
        return self.__current_player

    def get_team_point(self):
        return self.team_point

    def __str__(self):
        data = f"Team {self.team_name}\n"
        data += f"Team Points: {self.team_point}\n"
        for player in self.__player_list:
            data += f"{player.get_name()}: Wins = {player.get_num_wins()}: Plays = {player.get_num_plays()}: Hand = {player.get_hand()} \n"
        return data
