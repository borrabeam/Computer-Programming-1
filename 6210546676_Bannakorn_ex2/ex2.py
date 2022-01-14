import math

# 1

# spin = input('Spin: ')
# charge = input('Charge: ')

# particle_list = ["Strange","Charm","Electron","Neutrino","Photon"]
# class_list = ["Quark","Lepton","Boson"] 

    
# if spin == '1/2' and charge == '-1/3':
#     print(particle_list[0],class_list[0])
# elif spin == '1/2' and charge == '2/3':
#     print(particle_list[1],class_list[0])
# elif spin == '1/2' and charge == '-1':
#     print(particle_list[2],class_list[1])
# elif spin == '1/2' and charge == '0':
#     print(particle_list[3],class_list[1])
# elif spin == '1' and charge == '0':
#     print(particle_list[4],class_list[2])
# else:
#     pass


# ---------------------------------------------

# 2

# first_number = float(input('First number: '))
# second_number = float(input('Second number: '))
# operation = input('Operation: ')

# if operation == '+':   
#     print(first_number + second_number)
# elif operation == '-':
#     print(first_number - second_number)
# elif operation == '*':
#     print(first_number * second_number)
# elif operation == 'pow':
#     print(first_number ** second_number)
# elif operation == '/':
#     if second_number == 0:
#         print('Division by 0!')
#     else:
#         print(first_number / second_number)
# elif operation == 'mod':
#     if second_number == 0:
#         print('Division by 0!')
#     else:
#         print(first_number % second_number)
# elif operation == 'div':
#     if second_number == 0:
#         print('Division by 0!')
#     else:
#         print(first_number // second_number)
# else:
#     pass

# --------------------------------------------------
  
# 3

# money = float(input('Your money: '))


# chicken = 23
# goat = 678
# pig = 1296
# cow = 3848
# sheep = 6769

# if money < 23:
#     print('None')
#     # chicken
# elif money == 23:
#     print(f'{money / chicken:.0f} chicken')
# elif 23 < money < 678:
#     print(f'{money / chicken:.0f} chickens')
# elif money == 678:
#     print(f'{money / goat:.0f} goat')
# elif 678 < money < 1296:
#     print(f'{moeny / goat:0f} goats')
# elif money == 1296:
#     print(f'{money / pig:.0f} pig')
# elif 1296 < money < 3848:
#     print(f'{money / pig:.0f} pigs')
# elif money == 3848:
#     print(f'{money / cow:.0f} cows')
# elif 3848 < money < 6769:
#     print(f'{money / cow:.0f} cows')
# elif money > 6768:
#     print(f'{money / sheep:.0f} sheep')
# else:
#     pass

# ------------------------------------------

# 4

# offset = float(input('Offset: '))

# if offset == 0:
#     print('Tuesday')
# elif offset >= +1 and offset < +13.30:
#     print('Tuesday')
# elif offset >= 13.30 and offset <= +14:
#     print('Wednesday')
# elif offset <= -1 and offset >= -10.30:
#     print('Tuesdays')
# elif offset < -10.30 and offset >= -12 :
#     print('Monday')

# --------------------------------------------

# 5

# def is_even(number):
#     number = int(input('Number: '))

#     if number % 2 == 0:
#         print('True')
#     else:
#         print('False')
    

# is_even('number')

# ----------------------------------------------

# 6

# def is_leap_year(year):
#     year = int(input('Year: '))

#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('True')
#     else:
#         print('False')
    

# is_leap_year('year')

# 7

# def interval_intersect(a,b,c,d):
#     a = int(input('a: '))
#     b = int(input('b: '))
#     c = int(input('c: '))
#     d = int(input('d: '))
#     if b > c and d > a:
#         print('True')
#     else:
#         print('False')

# interval_intersect('a','b','c','d')

# 8
# def print_digits(number):
#     number = int(input('Pick a number between 1 to 100: '))
#     if 0 <= number  < 100:
#         print(f'The tens digit is {number // 10} and the ones digits is {number % 10}')
#     else:
#         print('Error: Input is not a two-digit number.')
    
#     return number

# print_digits('number')

# -------------------------------------

# 9

# def smaller_root(a,b,c):
#     a = int(input('a: '))
#     b = int(input('b: '))
#     c = int(input('c: '))

#     first_step = (b**2)-(4*a*c)

#     if first_step == 0:
#         x = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
#         print(x)
#     elif first_step > 0:
#         x = (-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
#         y = (-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
#         print(x , y)
#     else:
#         print('Error: No real solutions')
#         pass
#     return a,b,c


# smaller_root('a','b','c')

# ----------------------------------------

# 10


# def there_is_odd(x,y,z):

#     x = int(input('x: '))
#     y = int(input('y: '))
#     z = int(input('z: '))

    
#     if x % 2 == 1:
#         print(f'There is an odd number whose value is {x}')
#     elif y % 2 == 1:
#         print(f'There is an odd number whose value is {y}')
#     elif z % 2 == 1:
#         print(f'There is an odd number whose value is {z}')
#     else:
#         print('There is no odd number')
    

# there_is_odd('x','y','z')
    
# 11

# def list_all_odds(w,x,y,z):
#     w = int(input('w: '))
#     x = int(input('x: '))
#     y = int(input('y: '))
#     z = int(input('z: '))

#     if x % 2 == 0 and y % 2 == 0 and z % 2 ==0:
#         print('There is no odd number')
#     if w % 2 == 1:
#         print(f'This value is odd {w}')
#     if x % 2 == 1:
#         print(f'This value is odd {x}')
#     if y % 2 == 1:
#         print(f'This value is odd {y}')
#     if z % 2 == 1:
#         print(f'This value is odd {z}')

# list_all_odds('w','x','y','z')


# 12

# def max_of_three(x,y,z):
    
#     x = int(input('x: '))
#     y = int(input('y: '))
#     z = int(input('z: '))

#     if x > y and x > z:
#         print(f'The max value is {x} ')
#     elif y > x and y > z:
#         print(f'The max value is {y} ')
#     elif z > x and z > y:
#         print(f'The max value is {z} ')
#     else:
#         pass

# max_of_three('x','y','z')



    
















