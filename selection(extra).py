# import sys

# 1

# def is_triangle(a,b,c):
#     if a+b > c and a+c > b and c+b > a:
#         return True
#     else:
#         return False

# def read_nonnegative(msg):
#     a = float(input(msg))

#     if a < 0 :
#         print("Invalid value: input must be nonnegative")
#         sys.exit()
#     else:
#         return a

# a = read_nonnegative("Enter 1st line's length: ")
# b = read_nonnegative("Enter 2nd line's length: ")
# c = read_nonnegative("Enter 3rd line's length: ")

# if is_triangle(a,b,c):
#     print("It's a triangle.")
# else:
#     print("It's not a triangle.")

# -------------------------------------
# 2

# x = float(input('Enter x: '))
# y = float(input('Enter y: '))

# if 5 < x <=20:
#     a = 4*x*y + 5
# else:
#     a = (x**2) - (100*y)

# print(f'f({x:.3f},{y:.3f}) = {a:.3f} ')

# -----------------------------

# 3
def min_of_three(a,b,c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c

