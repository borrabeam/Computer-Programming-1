import urllib.request
import csv
import codecs
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
team_list = []
for i in data_str:
    team_list.append(i)
# print(team_list)




home_team = []
away_team = []
home_goal = []
away_goal = []
llist = []
mp_list = []
win_list = []
win_team = []
lose_team = []


for i in team_list:
    home_team.append(i[0])
    away_team.append(i[1])
    home_goal.append(i[2])
    away_goal.append(i[3])

home_team.remove(home_team[0])
away_team.remove(away_team[0])
home_goal.remove(home_goal[0])
away_goal.remove(away_goal[0])




def team():
    
    for i in home_team:
        if i not in llist:
            llist.append(i)
        else:
            pass

def mp():
    
    for i in llist:
        match_play = 1
        home_team.remove(home_team[0])
        
        if i in home_team:
            match_play += 1
        if i in away_team:
            match_play += 1
        
        mp_list.append(match_play)
            

        # match_play = 0
        # mp_list.append(match_play)
        # if i in home_team:
        #     mp_list[i] += 1
        # if i in away_team:
        #     mp_list[i] += 1
        
# def win():
    
#     for i in range(len(home_team)):

#         if home_goal[i] > away_goal[i]:
#             win_team.append(home_team[i])
#             lose_team.append(away_team[i])
#         elif home_goal[i] < away_goal[i]:
#             win_team.append(away_team[i])
#             lose_team.append(lose_team[i])
#         else: pass

#     for i in win_team:
#         win = 1
#         win_team.remove(win_team[0])
#         if i in win_team:
#             win += 1
#         win_list.append(win)

    
    



team()
mp()
# win()
# print(win_list)

while True:
    input1 = input('(S)how (Q)uit : ')
    if input1 == 's' or input1 == 'S':
        for i in range(len(llist)):
            print(f"{i+1}.{llist[i]} {mp_list[i]}")
        # for i in range(len(home_team)-1):
        #     print(f"{i+1}.{home_team[i+1]}({home_goal[i+1]}){away_team[i+1]}({away_goal[i+1]})")
    elif input1 == 'q' or input1 == 'Q':
        print("Bye")
        break
    else:
        print('Incorrect Menu')
        