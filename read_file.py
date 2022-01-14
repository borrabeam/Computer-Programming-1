import sys
name = []
win = []
lose = []
win_rate = []


file_name = input('Enter a file name: ')
f = open(f"{file_name}",'r').readlines()



for i in range(len(f)):
    g = f[i].split(',')
    name.append(g[0])
    win.append(g[1])
    lose.append(g[2])

def append(win,lose):
    
    for i in range(len(f)):
        wr = int(win[i]) / (int(win[i]) + int(lose[i])) 
        win_rate.append(wr)
    return win_rate

def max_to_min(wr):
    dict1 = {}
    
    for i in range(len(f)):
        dict1[name[i]] = win_rate[i]
    sort_dict1 = sorted(dict1.items(), key = lambda x: x[1], reverse=True)
    print(sort_dict1)

    for i in sort_dict1:
        print(f'{i[0]}: got win rate {i[1]:.5f}')
    
    



def min_to_max(wr):
    dict1 = {}
    
    for i in range(len(f)):
        dict1[name[i]] = win_rate[i]
    sort_dict1 = sorted(dict1.items(), key = lambda x: x[1])

    
    for i in sort_dict1:
        print(f'{i[0]}: got win rate {i[1]:.5f}')
    
    

    

wr = append(win,lose)


maxx = max(win_rate)
minni = min(win_rate)

index_max = 0
index_min = 0

def max_():
    global index_max,input1,maxx
    for i in range(len(win_rate)):
        if (win_rate[i] == maxx) :
            index_max = i
            print(f'{name[index_max]} got maximum win rate: {maxx:.5f} ' )
    
def min_():
    global index_min,input1,minni

    for i in range(len(win_rate)):
        if (win_rate[i] == minni) :
            index_min = i
            print(f'{name[index_min]} got maximum win rate: {minni:.5f} ' )
    #     
    #     elif (win_rate[i] == minni):
    #         index_min = i
    #         print(f'{name[index_min]} got minimum win rate: {minni:.5f}')
    
    
# print('==========')






while True:
    input1 = input('What do you want to know ? (m)in , ma(x), (o)rder max to min, o(r)der min to max, (q)uit : ')
    if input1 == 'm' or input1 == 'M': 
        min_()
    elif input1 == 'x' or input1 == 'X':
        max_()
    elif input1 == 'o' or input1 == 'O':
        print(f'Total team(s): {len(f)}')
        max_to_min(wr)
    elif input1 == 'r' or input1 == 'R':
        print(f'Total team(s): {len(f)}')
        min_to_max(wr)
    elif input1 == 'q' or input1 =='Q':
        print('Bye')
        sys.exit()
    else:
        pass