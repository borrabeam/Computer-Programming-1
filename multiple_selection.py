

# # 1

# weight = int(input('Please enter your weight in kg: '))
# height = int(input('Please enter your hegith in cm: '))
# bmi = weight/ (height/100)**2

# print(f'Your BMI is {bmi:.2f}')
# if bmi < 18.5:
#     print(f'Weight status: underweight')
# elif 18.5 <= bmi < 25:
#     print(f'Weight status: normal')
# elif 25 <= bmi < 30:
#     print(f'Weight status: overweight')
# else: 
#     print(f'Weight status: obese')

# ---------------------------------

# 2

# hw = int(input('What is the homework percentage? '))
# mt = int(input('What is the midterm percentage? '))
# fn = int(input('What is the final percentage? '))

# hw = hw*0.1
# mt = mt*0.2
# fn = fn*0.7

# score = hw+mt+fn

# print(f'Your total score is {score:.2f}')
# if score >= 80:
#     print('You receive the grade A')
# elif 75 <= score < 80:
#     print('You receive the grade B+')
# elif 70 <= score < 75:
#     print('You receive the grade B')
# elif 65<= score < 70:
#     print('You receive the grade C+')
# elif 60<= score < 65:
#     print('You receive the grade C')
# elif 55<= score < 60:
#     print('You receive the grade D+')
# elif 50<= score < 55:
#     print('You receive the grade D')
# else:
#     print('You receive the grade F')


# -------------------------------------------

# 3

# leap = int(input("Enter year in AD: "))
# if leap <= 0:
#     print("Invalid input: use positive integer")
# elif 1 <= leap <= 1752:
#     if leap % 4 == 0:
#         print(f"AD {leap} is a leap year")
#     else:
#         print(f"AD {leap} is not a leap year")
# elif leap > 1752:
#     if leap % 4 == 0 and leap % 100 != 0 or leap % 400 == 0:
#         print(f"AD {leap} is a leap year")
#     else:
#         print(f"AD {leap} is not a leap year")










# multiply selection extra


# 1

# real_num = float(input('Enter a real number: '))

# if real_num <= 15:
#     x = real_num*2 + 10
#     print(f'f({real_num:.3f}) = {x:.3f}')
# elif 15 < real_num <= 35:
#     x = 3*(real_num**2)
#     print(f'f({real_num:.3f}) = {x:.3f}')
# else:
#     x = 2*(real_num**3) - 5
#     print(f'f({real_num:.3f}) = {x:.3f}')


# ---------------------

# 2

# print('Input a point (x,y):')
# x = float(input('x = ? '))
# y = float(input('y = ? '))


# if x == 0 and y == 0:
#     print(f"The point ({x:.2f},{y:.2f}) is at the origin.")
# elif y == 0 :
#     print(f"The point ({x:.2f},{y:.2f}) is on the x-axis.")
# elif x == 0 :
#     print(f"The point ({x:.2f},{y:.2f}) is on the y-axis.")
# elif x > 0 and y > 0:
#         print(f"The point ({x:.2f},{y:.2f}) is in quadrant 1.")
# elif x < 0 and y >0 :
#         print(f"The point ({x:.2f},{y:.2f}) is in quadrant 2.")
# elif x <0 and y<0 :
#     print(f"The point ({x:.2f},{y:.2f}) is in quadrant 3.")
# else:
#     print(f"The point ({x:.2f},{y:.2f}) is in quadrant 4.")


# ----------------


# 3


# def is_right_triangle(a,b,c):
#     if a+b>c and a+c>b and b+c>a:
#         if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
#             print("It's a right triangle.")
#         else:
#             print("It's a triangle but not a right triangle.")
#     else:
#         print("It's not a triangle.")

# side1=float(input("Enter 1st line's length: "))
# side2=float(input("Enter 2nd line's length: "))
# side3=float(input("Enter 3rd line's length: "))

# is_right_triangle(side1,side2,side3)


msg = 'Python is fun'
chars = list(msg)
print(chars)
['P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'f', 'u', 'n']
['P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'f', 'u', 'n']