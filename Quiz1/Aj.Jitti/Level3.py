
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

    
    
   

import urllib.request
import csv
import codecs

csv_url = "http://eduserv.ku.ac.th/EPL2020.csv"
data_byte = urllib.request.urlopen(csv_url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))   


short_name_list = []
full_name_list = []
win_list = []
draw_list = []
lose_list = []

def append():
    for i in data_str:
        short_name_list.append(i[0])
        full_name_list.append(i[1])
        win_list.append(i[2])
        draw_list.append(i[3])
        lose_list.append(i[4])
append()
for i in range(len(short_name_list)):
        print(f"{short_name_list[i]},{full_name_list[i]},{win_list[i]},{draw_list[i]},{lose_list[i]}")