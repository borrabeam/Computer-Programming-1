

# n = 1
# sum = 0
# while True:
#     num = int(input(f'Enter value{n}: '))
#     if num == -99:
#         break
#     n += 1
#     sum += num

# print(f'You entered {n-1} numbers')
# print(f'Sum of them = {sum}')



# 3

# n = 1
# sum = 0
# x = []
# while True:
#     num = int(input(f'Enter value{n}: '))
#     if num == -99:
#         break
#     n += 1
#     sum += num
#     x.append(num)
# print(x)
# print(f'{sum / (n-1):.2f}')

# 4

# def read_list_while():
#     n = 1
#     sum = 0
#     llist1 = []
#     while True:
#         num = int(input(f'Enter value{n}: '))
#         if num == -99:
#             break
#         n += 1
#         sum += num
#         llist1.append(num)

#     return llist1



# llist1 = read_list_while()
# print(llist1)
# print(f'{sum(llist1)/len(llist1):.2f}')

# --------------------------------------------

# 5
# def read_list_while():
    
#     n = 1
#     sum = 0
#     llist1 = []``
#     while True:
#         num = int(input(f'Enter value{n}: '))
#         if num == -99:
#             break
#         n += 1
#         sum += num
#         llist1.append(num)

#     return llist1




# count = 1
# a = True
# while a == True:
#     print(f"Enter vector{count}: ")
#     llist1 = read_list_while()
#     print(f"Vector {count}:")
#     print(llist1)
#     print(f'{sum(llist1)/len(llist1):.2f}')
#     count += 1

# ------------------------------------------------
        
# # 6
# def read_list_while():
    
#     n = 1
#     sum = 0
#     llist = []
#     while True:
#         num = int(input(f'Enter value{n}: '))
#         if num == -99:
#             break
#         n += 1
#         sum += num
#         llist.append(num)

#     return llist





# def sum_vector(llist1,llist2):
#     llist3 = []
#     for number in range(len(llist1)):
#         sum_list = llist1[number] + llist2[number]
#         llist3.append(sum_list)
#     return llist3

# def diff_vector(llist1,llist2):
#     llist3 = []
#     for number in range(len(llist1)):
#         diff_llist = llist1[number] - llist2[number]
#         llist3.append(diff_llist)
#     return llist3

# def dot_product(llist1,llist2):
#     sum = 0
    
#     for number in range(len(llist1)):
#         diff_llist = llist1[number] * llist2[number]
#         sum += diff_llist
#     return  sum 


        
# print('Enter Vector 1: ')
# llist1 = read_list_while()
# print('Vector: 1')
# print(llist1)
# print('Enter Vector 2: ')
# llist2 = read_list_while()
# print('Vector: 2')
# print(llist2)
# print('Sum result: ')
# print(sum_vector(llist1,llist2))
# print('Diff result: ')
# print(diff_vector(llist1,llist2))
# print('Dot product: ')
# print(dot_product(llist1,llist2))

# # ---------------------------------------

# # 7


# def print_every_n(v1,n):        
#     count = 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
#     for i in v1:
#         count += 1
#         if count % n == 0:
#             print(i)
# def print_mod_n(v1,n):
#     for i in v1:
#         if i % n ==0:
#             print(i)

# def find_n(v1,n):
#     llist = []
#     count = 0
#     for i in v1:
#         if i == n:
#             llist.append(count)
#         count += 1
#     return llist



# v1 = [1,2,3,4,5,6,7,8,9,10,11,12,3,3,9,3,99]
# n = 3
# print('Initial Vector: ')
# print(v1)
# print(f'Print every {n}th number: ')
# print_every_n(v1,n)
# print(f'Print number divisible by {n}')
# print_mod_n(v1,n)
# print(f'Print list index of {n}')
# index_result = find_n(v1,n)
# print(index_result)