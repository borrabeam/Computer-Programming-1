import urllib.request
import csv
import codecs
url = "http://eduserv.ku.ac.th/epl.csv"
data_byte = urllib.request.urlopen(url)
data_str = csv.reader(codecs.iterdecode(data_byte, 'utf-8'))
list = []
for i in data_str:
    list.append(i)
#Before writing any code, you may uncomment the below line to see the result and learn how does the code work
# print(len(list))
# print(list)



home_team = []
away_team = []
home_goal = []
away_goal = []
team_list = []

def append():
    for i in list:
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
        if i not in team_list:
            team_list.append(i)
        else:
            pass
    
    team_list.sort()


def check_win_lose():
    for i in range(len(home_team)):
        if home_goal[i] > away_goal[i]:
            print(f"{i+1}.{home_team[i]} wins {away_team[i]} {home_goal[i]}:{away_goal[i]}")
        elif home_goal[i] < away_goal[i]:
            print(f"{i+1}.{home_team[i]} loses {away_team[i]} {home_goal[i]}:{away_goal[i]}")
        else:
            print(f"{i+1}.{home_team[i]} draws {away_team[i]} {home_goal[i]}:{away_goal[i]}")
    



append()
team()

while True:
    input1 = input('(M)atches (T)eams (R)esults (Q)uit : ')
    if input1 == 'm' or input1 == 'M':
        
        for i in range(len(home_team)-1):
            print(f"{i+1}.{home_team[i+1]}({home_goal[i+1]}){away_team[i+1]}({away_goal[i+1]})")
    elif input1 == 'q' or input1 == 'Q':
        print("Bye")
        break
    elif input1 == 't' or input1 == 'T':
        for i in range(len(team_list)):
            print(f"{i+1}.{team_list[i]} ")
    elif input1 == 'r' or input1 == 'R':
        check_win_lose()
    else:
        print('Incorrect Menu')
        

