import math


# hours = float(input('How many hours?: '))
# baht = float(input('How many Baht per hour?: '))

# fee = math.ceil(hours) *baht


# print(f'Parking fee is {fee:.2f} Baht.')



# 2

# ask = int(input('How many?: '))
# price = float(input('Price for each?: '))

# total_price = ask * price
# print(f'Total price is {total_price:.1f}')


# 3



# TV   = 3000
# Oven = 1500
# Fan  = 1000

# def cal_tv(amount,tv):
#     return amount*TV

# def cal_oven(amount,oven):
#     return amount*Oven

# def cal_fan(amount,fan):
#     return amount * Fan

# tv   = int(input("How many TVs?: "))
# oven = int(input("How many ovens?: "))
# fan  = int(input("How many fans?: "))
# print(f'Total price is {cal_tv(tv,TV) + cal_oven(oven,Oven) + cal_fan(fan,Fan)} Baht.')

# 4

# w = float(input('Enter w: '))
# l = float(input('Enter l: '))
# h = float(input('Enter h: '))

# surface = w*l*2 + l*h*2 + w*h*2
# volume = w*l*h

# print(f'Surface Area = {surface:.2f}')
# print(f'Volume = {volume:.2f}')

# 5

# def cal_surface_area(w,l,h):
#     surface = w*l*2 + l*h*2 + w*h*2
#     return surface
    

# def cal_volume(w,l,h):
#     volume = w*l*h
#     return volume
    

# w = float(input('Enter w: '))
# l = float(input('Enter l: '))
# h = float(input('Enter h: '))

# print(f'Surface Area = {cal_surface_area(w,l,h):.2f}')
# print(f'Volume = {cal_volume(w,l,h):.2f}')


# 6

# def cal_surface_area(w,l,h):
#     surface = w*l*2 + l*h*2 + w*h*2
#     return surface
    

# def cal_volume(w,l,h):
#     volume = w*l*h
#     return volume
    

# def user_input():

#     w = float(input('Enter w: '))
#     l = float(input('Enter l: '))
#     h = float(input('Enter h: '))
#     return w,l,h
    

# def print_report(w,l,h):
#     print(f'Surface Area = {cal_surface_area(w,l,h):.2f}')
#     print(f'Volume = {cal_volume(w,l,h):.2f}')
    

# w,l,h = user_input()
# print_report(w,l,h)


# 7

import math
def check_unit (final):
    if final <= 1:
        print('square meter')
    else:
        print('square meters')
    """Check plural (square meter or square meters)"""
    
def cal_circle ():
    r = float(input('Radius = '))
    final = r * 3.14
    return final
    
    """Calculate and return area result)"""
    
def cal_triangle():
    b = float(input('base = '))
    h = float(input('height = '))
    final = (1/2)*b*h
    return final
    """Calculate and return area result)"""
    
def cal_rectangle ():
    b = float(input('base = '))
    h = float(input('height = '))
    final = (1/2)*b*h
    return final
    
    
    """Calculate and return area result)"""
    
def print_result (x,final,check_unit):
    """Print the area result with correct unit(s)"""
    print(f'Area of this {x} is {final} {check_unit}. ')


menu = input("(T)riangle (R)ectangle (C)ircle : ")
if menu == 't' or menu == 'T':
    cal_triangle()  
    print_result('triangle',check_unit)
elif menu == 'r' or menu =='R':
    cal_rectangle()
    print_result('rectangle','area')
elif menu == 'c' or menu == 'C':
    cal_circle()
    print_result('circle','area')
else:

    print("Incorrect Input!")
