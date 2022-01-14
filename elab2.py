from math import pi
import math
import sys
# elab 2


# ad = input('Enter a year in A.D.: ')
# be = int(ad) + 543
# print('The year in B.E. is ' + str(be))

# -----

# width = float(input('Enter rectangle\'s width: '))
# height = float(input('Enter rectangle\'s height: '))
# print('The area of the rectangle is ' +str(width*height))

# -----

# total = 50+60+125+300+80+300+90
# discount = float(total*0.85)
# print(f'The discounted cost is {discount:.2f}')

# -----

# times = int(input('How many seconds have passed? '))
# hours = times//3600
# minutes = (times%3600)//60
# seconds = times%60
# print(f'{hours} hour(s) {minutes} minute(s) and {seconds} second(s) have passed.')

# -----

# x = int(input('Enter x: '))
# y = int(input('Enter y: '))

# r_1 = (x-y)/(x+y)
# r_2 = 3.14/(0.15+(y/x))
# r_3 = r_1*r_2

# print(f'The result is {r_3:.5f}')


# -----

# width = int(input('Enter width: '))
# length = int(input('Enter length: '))
# size = (width*length)//100

# print(f'The landlord will have {size} of land available for sale.')


# ----------

# name1 = input("Enter name #1: ")
# gpa1 = float(input("Enter GPA #1: "))
# name2 = input("Enter name #2: ")
# gpa2 = float(input("Enter GPA #2: "))

# print(f"+-----------+-------+")
# print(f"|   Name    |  GPA  |")
# print(f"+-----------+-------+")
# print(f"| {name1:<9}   | {gpa1:<1.2f}|")
# print(f"| {name2:<9}   | {gpa2:<1.2f}|")
# print(f"+-----------+-------+")


# ---------------------------------------------------------------------------------------------------------------

# elab4




# def circle_circumference(r):
#     c = 2*pi*r
#     return c

# def circle_area(r):
#     a = pi*(r**2)
#     return a

# r = float(input('Enter circle radius: '))






# circumference = circle_circumference(r)
# area = circle_area(r)
# print(f'Circle circumference is {circumference:.2f}')
# print(f'Circle area is {area:.2f}')

# ---------------

# def green_area(x,y):
#     a = x*y
#     return a

# def cal_circle(d):
#     b = pi*(d/2)**2
#     return b


# x = float(input('Enter x: '))
# y = float(input('Enter y: '))
# d = float(input('Enter d: '))

# print(f'The area of the lawn is {green_area(x,y) - cal_circle(d):.2f} sq.m. ')

# -------------

# parking = int(input('Enter parking time in minutes: '))

# fee = math.ceil(parking/60) *25
# print(f'Parking fee is {fee} baht.')


# -------------

# def future_value(initial,interest,years):
#     return initial*(1+interest/100)**years

# initial = int(input('Enter initial amount in Baht: '))
# interest = int(input('Enter interest rate in percent: '))

# print(f'Total amount after 1 year is {future_value(initial,interest,1):.2f} Baht.')
# print(f'Total amount after 5 years is {future_value(initial,interest,5):.2f} Baht.')
# print(f'Total amount after 10 years is {future_value(initial,interest,10):.2f} Baht.')
# print(f'Total amount after 20 years is {future_value(initial,interest,20):.2f} Baht.')


# -----
# def bmi(weight,height):
#     return weight/((height/100)**2)


# weight = float(input('Please enter your weight (in kg): '))
# height = float(input('Please enter your height (in cm): '))


# mass = bmi(weight,height)
# print(f'Your Body Mass Index (BMI) is {mass:.2f}')


# --------------
# def print_hello(name):
#     print('Hello,' + name)
#     return name



# --------------


# def ask_length_height():
#     a = float(input('What is the length of side a: '))
#     b = float(input('What is the length of side b: '))
#     height = float(input('Enter height: '))
#     return a,b,height

# def area_trap(a,b,height):
#     area = ((a+b)/2)*height
#     return area
# print("Specify your trapezoid's properties.")
# a,b,height = ask_length_height()
# area = area_trap(a,b,height)
# print(f'The area of the trapezoid is {area:.2f}')


# ----------------
# KILOMETERS_PER_MILE =  1.609

# def miles_to_kilometers(miles):
#     distance = miles*KILOMETERS_PER_MILE
#     return distance

# miles = float(input('Enter the distance in miles: '))
# distance = miles_to_kilometers(miles)
# print(f'The distance is {distance:.2f} kilometers.')

# --------------

# def read_vector(msg):
#     print(msg)
#     x = float(input('x = '))
#     y = float(input('y = '))
#     return x,y

# def dot_product(x1,y1,x2,y2):
#     dot = (x1*x2)+(y1*y2)
#     return dot

# x1,y1 = read_vector('Enter vector A: ')
# x2,y2 = read_vector('Enter vector B: ')
# print(f'Dot product of A and B is {dot_product(x1,y1,x2,y2):.2f}')


# ----------------

# def formula1(a,b,c):
#     s = (a+b+c)/2
#     return s

# def formula2(s,a,b,c):
#     result = math.sqrt(s*(s-a)*(s-b)*(s-c))
#     return result

# def question():

#     a = float(input('Enter length of side 1: ')) 
#     b = float(input('Enter length of side 2: ')) 
#     c = float(input('Enter length of side 3: ')) 
#     return a,b,c
# a,b,c = question()
# s = formula1(a,b,c)
# print(f'Area of the triangle is {formula2(s,a,b,c):.2f}')

# same

# a = float(input('Enter length of side 1: ')) 
# b = float(input('Enter length of side 2: ')) 
# c = float(input('Enter length of side 3: '))

# s = (a+b+c)/2

# result = math.sqrt(s*(s-a)*(s-b)*(s-c))
# print(f'Area of the triangle is {result:.2f}')


# --------------------------


# TV = 9000
# DVD_player = 2250
# Audio_system = 4500


# num_tv = int(input(f'Number of TVs: '))
# num_dvd = int(input(f'Number of DVD players: '))
# num_audio = int(input(f'Number of audio systems: '))

# total = (num_tv*TV) + (num_dvd*DVD_player) + (num_audio*Audio_system)
# discount = total*0.2

# if total >= 30000:
#     print(f'The total amount is {total:.2f} baht.')
#     print(f'You got a discount of {discount:.2f} baht.')
#     print(f'Your payment is {total-discount:.2f} baht. Thank you.')
# else:
#     print(f'The total amount is {total:.2f} baht.')
#     print(f'Your payment is {total:.2f} baht. Thank you.')


# --------------------------------------

# def more_than_zero():
#     x = (-b+(d**0.5))/(2*a)
#     y = (-b-(d**0.5))/(2*a)
#     return x,y
# def less_eq_zero():
#     x = (-b)/(2*a)
#     if d < 0:
#         x1 = (-b)/(2*a) + (math.sqrt(-d)/(2*a))
#         x2 = (-b)/(2*a) - (math.sqrt(-d)/(2*a))
#         return x1,x2
#     else: 
#         return x

# a = float(input("Enter 1st coefficient: "))
# if a == 0:
#     print("1st coefficient can't be zero. Program exits.")
#     sys.exit()
# b = float(input("Enter 2nd coefficient: "))
# c = float(input("Enter 3rd coefficient: "))
# d = (b**2)-(4*a*c)
# if d > 0:
#     x,y = more_than_zero()
#     print(f"Two real roots: {x:.3f} and {y:.3f}")
# elif d == 0:
#     x = less_eq_zero()
#     print(f"Only one real root: {x:.3f}")
# else : 
#     x1,x2 = less_eq_zero()
#     print(f"Two complex roots: {x2:.3f}+{abs(x1):.3f}i and {x2:.3f}-{abs(x1):.3f}i")

# ---------------------------



