import sys,cmath

def more_than_zero():
    x = (-b+(d**0.5))/(2*a)
    y = (-b-(d**0.5))/(2*a)
    return x,y
def less_eq_zero():
    x = (-b)/(2*a)
    if d < 0:
        x1 = (-b)/(2*a) + (-d**0.5)/(2*a)
        x2 = (-b)/(2*a) - (-d**0.5)/(2*a)
        return x1,x2
    else: return x

a = float(input("Enter 1st coefficient: "))
if a == 0:
    print("1st coefficient can't be zero. Program exits.")
    sys.exit()
b = float(input("Enter 2nd coefficient: "))
c = float(input("Enter 3rd coefficient: "))
d = (b**2)-(4*a*c)
if d > 0:
    x,y = more_than_zero()
    print(f"Two real roots: {x:.3f} and {y:.3f}")
elif d == 0:
    x = less_eq_zero()
    print(f"Only one real root: {x:.3f}")
else : 
    x1,x2 = less_eq_zero()
    print(f"Two complex roots: {x1.real:.3f}+{abs(x1.imag):.3f}i and {x2.real:.3f}-{abs(x2.imag):.3f}i")


