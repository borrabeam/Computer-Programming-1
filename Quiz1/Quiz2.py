from math import pi

all =['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

def triangle():
    
   
    
    while True:
        b = input('base = ')
        if b not in all:
            h = input('height = ')
            if h not in all:
                break
            else:
                print('Please enter a number!')
        else:
            print('Please enter a number!')

        


    final = (1/2)*(float(b)*float(h))
    if final <= 1:
        print(f'Area of this triangle is {final:.2f} square meter.')
    else:
        print(f'Area of this triangle is {final:.2f} square meters.')

def rectangle():
    

    while True:
        w = input('width = ')
        if w not in all:
            h = input('height = ')
            if h not in all:
                break
            else:
                print('Please enter a number!')
        else:
            print('Please enter a number!')


    final = (float(w) * float(h))
    if final <= 1:
        print(f'Area of this rectangle is {final:.2f} square meter.')
    else:
        print(f'Area of this rectangle is {final:.2f} square meters.')

def circle():
    while True:
        r = input('Radius = ')
        if r not in all:
            break
        else:
            print('Please enter a number!')
    
    
    final = pi * (float(r)**2)
    if final <= 1:
        print(f'Area of this circle is {final:.2f} square meter.')
    else:
        print(f'Area of this circle is {final:.2f} square meters.')
    

while True:
    choice = input('(T)riangle (R)ectangle (C)ircle (Q)uit : ')

    if choice == 't' or choice == 'T':
        triangle()
    elif choice == 'r' or choice == 'R':
        rectangle()
    elif choice == 'c' or choice == 'C':
        circle()
    elif choice == 'q' or choice == 'Q':
        print('Bye')
        break
    else:
        print('Incorrect Input')