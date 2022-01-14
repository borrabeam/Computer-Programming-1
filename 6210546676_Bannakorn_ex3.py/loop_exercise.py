def fib(n):
    """This function prints a Fibonacci sequence up to the nth Fibonacci"""
    
    n1 , n2 = 1 ,1
    count = 0
    
    while count <= n:
       print(n1, end=' ')
       n3 = n1 + n2
       
       n1 = n2
       n2 = n3
       count += 1

# fill me in

print("fib(n) result:")
n = 0
while n < 10:
    fib(n)
    print("")
    n += 1




def diamond(n):
    """This function prints a diamond shape of size n as shown in loop_exercise_result.txt"""
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("*" * (i * 2 + 2), end="")
        print(" " * (n - i - 1))
    for i in range(n - 1, -1, -1):
        print(" " * (n - i - 1), end="")
        print("*" * (i * 2 + 2), end="")
        print(" " * (n - i))



# fill me in

print("diamond(n) result:")
for i in range(0,8):
    diamond(i)
    print("")

def hailstone(n):
    """This function prints a hailstone sequence whose details can be found in this link:
        http://mathworld.wolfram.com/CollatzProblem.html"""
    
    count = 0
    while n != 1:
        print(f'{n:.0f}', end = ' ')
        if n % 2 == 0:
            n = n/2
            count += 1
        elif n % 2 == 1:
            n = (3 * n) +1
            count += 1
    else:
        print(f'{n:.0f}', end=' ')
        count += 1
        



# fill me in

print("hailstone(n) result:")
for i in range(1, 8):
    hailstone(i)
    print("")




def arith_sum(n):
    """This function prints the arithmetic sequence starting from 1 to nth together with its sum"""
    sum = 0
    for i in range(1, n+1):
        print(i, end=' ')
        sum += i
        if i == n:
            print('=', end=' ')
            
            print(f'{sum}')       
        else:
            print('+', end=' ')

# fill me in

print("arith_sum(n) result:")
for i in range(1, 10):
    arith_sum(i)
    print("")  