from math import pi
def green_area(x,y):
    a = x*y
    return a

def cal_circle(d):
    b = pi*(d/2)**2
    return b

x = float(input('Please enter x: '))
y = float(input('Please enter y: '))
d = float(input('Please enter d: '))

print(f'The Area of the lawn is {green_area(x,y) - cal_circle(d):.2f} sq.m.')