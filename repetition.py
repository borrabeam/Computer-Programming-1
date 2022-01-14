
# msg = input("What do you want me to say? ")
# num = int(input("How many times you want me to say it? "))


# for i in range(1,num+1,1):
#     print(f'{msg} #{i}')


# ----------------------------------------

# 2

# import math

# def f(n):
#     return 15 + 10*math.sin(n/10)

# print("  n | f(n)")
# print("----+-------------------------------------------------")
# for n in range(0,100,5) :
#     spaces = " " * round(f(n))
#     print(f" {n:2} | {spaces}*")

# -------------------------------------------------------------------------

# -------------------

# msg = input("Enter a message: ")

# out = ""
# for i in range(0,len(msg), 2):
#     out = out+msg[i]
# print(out)

# out = ""
# for i in range(1,len(msg), 2):
#     out = out+msg[i]
# print(out)
# Programming is fun

# -------------------------------------

# msg = input("Enter a message: ")
# for i in range(len(msg)) :
#     print(f"Character {i+1} is {msg[i]}")

# -----------------------------------------

# 4
# block = int(input('Enter the size of block: '))
# character = input('Enter the character to use: ')

# for i in range(block):
#     print(f"{character * block}")

# ----------------------------------------------------------

# 5

character = input('Enter a string: ')

for i in range(len(character)):
    print(f"{i * ' '}{character[i]}")
   