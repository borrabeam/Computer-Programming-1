msg = 'Good evening'
seq = list(msg)
seq.reverse()
print(seq)

x = [1,2,3,4,5]
y = x
z = [1,2,3,4,5]
print(x)
# [1, 2, 3, 4, 5]
print(y)
# [1, 2, 3, 4, 5]
print(z)
# [1, 2, 3, 4, 5]
x[3] = 200
print(x)
# [1, 2, 3, 200, 5]
print(y)
# [1, 2, 3, 200, 5]
print(z)
# [1, 2, 3, 4, 5]


seq = [2,3,5,7,11,13,17,19]
for i in range(0,5):
    print(seq[i])

seq = [2,3,5,7,11,13,17,19]
for i in range(7,-1,-1):
    print(seq[i])


# --------------------------------

# 4 score statistics


# 4


llist1 = []
summ = 0

def average(summ):
    a = summ/len(llist1)
    return a
def minimun():
    a = min(llist1)
    return a
def maximum():
    a = max(llist1)
    return a


while True:
    score = input('Input student score (or just ENTER to finish): ')
    if score == '':
        break
    llist1.append(int(score))
    summ += int(score)    

for i in range(len(llist1)):
    print(f'Score #{i+1}: {llist1[i]}')

print(f'Average score is {average(summ):.2f}')
print(f'Minimum score is {minimun()}')
print(f'Maximum score is {maximum()}')

# ---------------------------------------------
# 5


llist1 = []

while True:
    score = input('Input student score (or just ENTER to finish): ')
    if score == '':
        break
    llist1.append(int(score))

for i in range(len(llist1)):
    llist1.sort(reverse= True)
    print(f'Rank #{i+1}: {llist1[i]}')


    print(f'Rank #{i+1}: {max(llist1)}')
    llist1.remove(max(llist1))



# --------------------------------------------------

# 6



def sd(llist1):
    a = 0

    for i in range(len(llist1)):
        a += (llist1[i]-(sum(llist1)/ len(llist1)))**2
    
    return (a/(len(llist1) - 1))**0.5


def grade(x,ave,sd):

    if x >= ave + 1.5*(sd):
        return 'A'
    elif x >= ave + 1.0*(sd):
        return 'B+'
    elif x >= ave + 0.5*(sd):
        return 'B'
    elif x >= ave:
        return 'C+'
    elif x >= ave -0.5*(sd):
        return 'C'
    elif x >= ave -1.0*(sd):
        return 'D+'
    elif x >= ave -1.5*(sd):
        return 'D'
    else:
        return 'F'




llist1 = []


while True:
    score = input('Input student score (or just ENTER to finish): ')
    if score == '':
        break
    llist1.append(int(score))

print(f'Average score is {sum(llist1)/ len(llist1):.2f}')
print(f'Standard deviation is {sd(llist1):.2f}')

for i in range(len(llist1)):
    
    print(f'Score #{i+1}: {llist1[i]} grade: {grade(llist1[i],sum(llist1)/ len(llist1),sd(llist1))}')






