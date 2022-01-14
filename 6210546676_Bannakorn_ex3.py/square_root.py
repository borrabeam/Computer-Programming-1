import math


def mysqrt(a):
    x = 4
    while True:       
        y = (x + a/x) /2
        if y == x:
            break
        x = y
    return y



def test_square_root():  
    for a in range(1,10):
       print(f"{a:.1f}  {mysqrt(a):<13.12}  {math.sqrt(a):<13.12}  {math.sqrt(a)-mysqrt(a)}")




print('a   mysqrt(a)       math.sqrt(a)   diff')
print('-   ------------    ------------   ----')       
test_square_root()



