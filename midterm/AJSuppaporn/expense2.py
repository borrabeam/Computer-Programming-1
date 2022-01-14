import sys

t1 = [50, 20, 30] 
t2 = [40, 25, 15.5] 
print('Teacher 1:') 
print(t1) 
print('Teacher 2:') 
print(t2)
print('Compute sum of some days...')

day_list = []

while True:
    day = int(input("Enter day number: "))
    if day == -99:
        break
    else:
        day_list.append(day)
        


teacher = int(input("Which teacher (1 or 2): "))
if teacher == 1:
    print(day_list)
    print(t1)
    summ = 0
    for i in range(len(day_list)):
        summ += t1[day_list[i]-1]
    print(f"Sum of Days {day_list} = {summ}")
else :
    print(day_list)
    print(t2)
    summ = 0
    for i in range(len(day_list)):
        summ += t2[day_list[i]-1]
    print(f"Sum of Days {day_list} = {summ:.2f}")

while True:
    con_input = input("Continue (y/n): ")
    if con_input == 'y':
        print('')
        print('Compute sum of some days...')
        day_list = []
        
        while True:
            day = int(input("Enter day number: "))
            if day == -99:
                break
            else:
                day_list.append(day)
                


        teacher = int(input("Which teacher (1 or 2): "))
        if teacher == 1:
            print(day_list)
            print(t1)
            summ = 0
            for i in range(len(day_list)):
                summ += t1[day_list[i]-1]
            print(f"Sum of Days {day_list} = {summ}")
        else :
            print(day_list)
            print(t2)
            summ = 0
            for i in range(len(day_list)):
                summ += t2[day_list[i]-1]
            print(f"Sum of Days {day_list} = {summ:.2f}")
    else:
        sys.exit()
    
    
