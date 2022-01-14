import sys

# name_list = []


# while True:
#     menu = input('(N)ew (Q)uit : ')
#     if menu == 'n' or menu == 'N':
#             name = input('Name: ')
#             print(f'{name} added')
#             name_list.append(name)
#             second_menu = input('(N)ew (S)how (Q)uit :')
#             break
#     elif menu == 'q' or menu == 'Q':
#             print('Bye')
#             sys.exit()
#     else:
#         print('Incorrect Menu')
        


# while True:
    
#     if second_menu == 'n' or menu == 'N':
#         name = input('Name: ')
#         print(f'{name} added')
#         name_list.append(name)
#         second_menu = input('(N)ew (S)how (Q)uit :')
#     elif second_menu == 's' or second_menu == 'S':
#         for i in range(len(name_list)):
#             print(f'{i+1} {name_list[i]}')
#         second_menu = input('(N)ew (S)how (Q)uit :')
#     elif second_menu == 'q' or menu == 'Q':
#         print('Bye')
#         sys.exit()
#     else:
#         print('Incorrect Menu')
#         second_menu = input('(N)ew (S)how (Q)uit :')
        
 


# ----------------------------------------------

# level 2


# import sys

# name_list = []


# while True:
#     menu = input('(N)ew (Q)uit : ')
#     if menu == 'n' or menu == 'N':
#             name = input('Name: ')
#             print(f'{name} added')
#             name_list.append(name)
#             second_menu = input('(N)ew (S)how (D)elete (Q)uit : ')
#             break
#     elif menu == 'q' or menu == 'Q':
#             print('Bye')
#             sys.exit()
#     else:
#         print('Incorrect Menu')
        


# while True:
    
#     if second_menu == 'n' or menu == 'N':
#         name = input('Name: ')
#         print(f'{name} added')
#         name_list.append(name)
#         second_menu = input('(N)ew (S)how (D)elete (Q)uit :' )
#     elif second_menu == 's' or second_menu == 'S':
#         for i in range(len(name_list)):
#             print(f'{i+1} {name_list[i]}')
#         second_menu = input('(N)ew (S)how (D)elete (Q)uit : ')
#     elif second_menu == 'q' or menu == 'Q':
#         print('Bye')
#         sys.exit()
#     elif second_menu == 'd' or second_menu == 'D':
#         number = int(input('Number? : '))

#         name_list.remove(name_list[number - 1])
#         second_menu = input('(N)ew (S)how (D)elete (Q)uit : ')
#     else:
#         print('Incorrect Menu')
#         second_menu = input('(N)ew (S)how (D)elete (Q)uit : ')
        
 
# ---------------------------------------------------------------------

# 3

# import sys

# name_list = []



# def first_menu():
#     global second_menu
#     while True:
#         menu = input('(N)ew (Q)uit : ')
#         if menu == 'n' or menu == 'N':
#             name = input('Name: ')
#             print(f'{name} added')
#             name_list.append(name)
#             second_menu = input('(N)ew (S)how (D)elete (Q)uit :' )
#             break
#         elif menu == 'q' or menu == 'Q':
#             print('Bye')
#             sys.exit()
#         else:
#             print('Incorrect Menu')
            

# first_menu()

# while True:
    
#     if second_menu == 'n' or second_menu == 'N':
#         name = input('Name: ')
#         print(f'{name} added')
#         name_list.append(name)
#         second_menu = input('(N)ew (S)how (D)elete (Q)uit :' )
#     elif second_menu == 's' or second_menu == 'S':
#         for i in range(len(name_list)):
#             print(f'{i+1} {name_list[i]}')
#         second_menu = input('(N)ew (S)how (D)elete (Q)uit : ')
#     elif second_menu == 'q' or second_menu == 'Q':
#         print('Bye')
#         sys.exit()
#     elif second_menu == 'd' or second_menu == 'D':
#         number = input('Number? : ')
#         while number.isdigit()==False:
#             print("Not a number")
#             number = input('Number? : ')
#         while len(name_list) < int(number) or int(number) <= 0:
#             print('Not in range')
#             number = input('Number? : ')
#         else: 
#             name_list.remove(name_list[int(number) - 1])
#             for i in range(len(name_list)):
#                 print(f'{i+1} {name_list[i]}')
#             if  not name_list:                  
#                 first_menu()
#             else:
#                 second_menu = input('(N)ew (S)how (D)elete (Q)uit : ')
#     else:
#         print('Incorrect Menu')
#         second_menu = input('(N)ew (S)how (D)elete (Q)uit : ')
        
# ----------------------------------------------------------------------

# 4
import sys

name_list = []



def menu_text():
    global second_menu
    while True:
        menu = input('(N)ew (Q)uit : ')
        if menu == 'n' or menu == 'N':
            name = input('Name : ')
            print(f'{name} added')
            name_list.append(name)
            second_menu = input('(N)ew (S)how (D)elete (Q)uit : ' )
            break
        elif menu == 'q' or menu == 'Q':
            print('Bye')
            sys.exit()
        else:
            print('Incorrect Menu')     

def new_item(name_list):
    global second_menu
    name = input('Name : ')
    print(f'{name} added')
    name_list.append(name)
    second_menu = input('(N)ew (S)how (D)elete (Q)uit : ' )
    
    



def show_item(name_list):
    global second_menu
    for i in range(len(name_list)):
        print(f'({i+1}) {name_list[i]}')
    second_menu = input('(N)ew (S)how (D)elete (Q)uit : ' )
    

def delete_item(name_list):
    global second_menu
    number = input('Number? : ')
    while number.isdigit()==False:
        print("Not a number")
        number = input('Number? : ')
    while len(name_list) < int(number) or int(number) <= 0:
        print('Not in range')
        number = input('Number? : ')
    else: 
        name_list.remove(name_list[int(number) - 1])
        for i in range(len(name_list)):
            print(f'({i+1}) {name_list[i]}')
        if not name_list:
            menu_text()
        else:
            second_menu = input('(N)ew (S)how (D)elete (Q)uit : ' )
    
            



menu_text()

while True:
    if second_menu == 'n' or second_menu == 'N':
        new_item(name_list)
        
    elif second_menu == 's' or second_menu == 'S':
        show_item(name_list)
    elif second_menu == 'q' or second_menu == 'Q':
        print('Bye')
        sys.exit()
    elif second_menu == 'd' or second_menu == 'D':
        delete_item(name_list)
    else:
        print('Incorrect Menu')
        second_menu = input('(N)ew (S)how (D)elete (Q)uit : ' )
        