import math

# 1

FEET_IN_MILE = 5280
miles = 13
feet = FEET_IN_MILE * miles
print(feet)


# 2

hours = 7*3600
minutes = 21*60
seconds = 37

total_sec = (hours+minutes+seconds)
print(total_sec)

# 3

width = 4
height = 7
cal_perimeter= (width*2) + (height*2)
print(f"The perimeter of a rectangle is {cal_perimeter}")

# 4

PI = 3.1415
radius = 8
cal = 2*PI*radius

print(cal)

# 5

present_value = 1000
annual_rate = 7
years = 10

future_value = present_value*(1+0.01*annual_rate)**years

print(future_value)

# 6

x0 = 2
y0 = 2
x1 = 5
y1 = 6

distance = math.sqrt((x0-x1)**2 + (y0-y1)**2)

print(distance)

# 7

x0 = 1
y0 = 1
x1 = 4
y1 = 1
x2 = 4
y2 = 5

a = math.sqrt((x0-x1)**2 + (y0-y1)**2)
b = math.sqrt((x1-x2)**2 + (y1-y2)**2)
c = math.sqrt((x2-x0)**2 + (y2-y0)**2)

s = 0.5*(a+b+c)
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(area)

# 8


amount_of_coffee = int(input('Write how many cups of coffee you will need: \n> '))

water = amount_of_coffee*200
milk = amount_of_coffee*50
coffee_beans = amount_of_coffee*15


print(f'For {amount_of_coffee} cups of coffee you will need: \n{water} ml of water \n{milk} ml of milk \n{coffee_beans} g of coffee beans.')




