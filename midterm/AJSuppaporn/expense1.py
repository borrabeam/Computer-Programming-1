

expense_list1 =[]
expense_list2 =[]
def compare_nums(x,y):
    if x < y:
        print(f'{x:.1f} is less than {y:.1f}')
    elif x > y:
        print(f'{x:.1f} is more than {y:.1f}')
    else:
        print(f'{x:.1f} is equal to {y:.1f}')

def read_list(day):
    print(f"Teacher 1:")
    for i in range(day):
        expense1 = float(input(f"Day {i+1}: enter expense: "))
        expense_list1.append(expense1)
    print(f"Teacher 2:")
    for i in range(day):
        expense2 = float(input(f"Day {i+1}: enter expense: "))
        expense_list2.append(expense2)
    print(expense_list1)
    print(expense_list2)

def print_list_comparison(expense_list1,expense_list2):
    for i in range(len(expense_list1)):
        if expense_list1[i] > expense_list2[i]:
            print(f"Day {i+1}: Teacher1 spends more than Teacher2")
        elif expense_list1[i] < expense_list2[i]:
            print(f"Day {i+1}: Teacher1 spends less than Teacher2")
        else:
            print(f"Day {i+1}: Teacher1 spends equal to Teacher2")

        


day = int(input("Enter #days: "))
read_list(day)
print_list_comparison(expense_list1,expense_list2)