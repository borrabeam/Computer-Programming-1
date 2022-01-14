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


for i in list:
    home_team.append(i[0])
    away_team.append(i[1])
    home_goal.append(i[2])
    away_goal.append(i[3])




while True:
    input1 = input('(M)atches (Q)uit : ')
    if input1 == 'm' or input1 == 'M':
        
        for i in range(len(home_team)-1):
            print(f"{i+1}.{home_team[i+1]}({home_goal[i+1]}){away_team[i+1]}({away_goal[i+1]})")
    elif input1 == 'q' or input1 == 'Q':
        print("Bye")
        break
    else:
        print('Incorrect Menu')
        

