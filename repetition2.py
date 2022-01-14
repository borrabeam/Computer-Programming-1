
# 2
# positive_list = []
# negative_list = []


# while True:
#     num = float(input("Enter a number (to exit, just enter zero): "))
#     if num == 0:
#         break
#     elif num > 0:
#         positive_list.append(num)
#     else:
#         negative_list.append(num)
        
# print(f"The sum of all positive numbers is {sum(positive_list):.2f}")
# print(f"The sum of all negative numbers is {sum(negative_list):.2f}")


# -----------------------------------------------------------------------------

        
# 3

# def fah_to_cel(start, end, step): # version 2
#     print(f"{'Fahrenheit':>12}{'Celcius':>12}")
#     print(f"{'----------':>12}{'-------':>12}")
#     fah = start
#     while fah < end and step > 0:
#         cel = (5/9)*(fah-32)
#         print(f"{fah:12.2f}{cel:12.2f}")
#         fah = fah + step
    
#     while fah > end and step < 0:
#         cel = (5/9)*(fah-32)
#         print(f"{fah:12.2f}{cel:12.2f}")
#         fah = fah + step
#     print(f"{'----------':>12}{'-------':>12}")

# fah_to_cel(20,15,-1)



# -----------------------------------------------------------------------------




# 4



# llist1 = []




# while True:
#     score = input('Enter a number (just [Enter] to exit): ')
#     if score == '':
#         if not llist1:
#             print("Nothing to do.")
#         else:
#             print(f'The maximum is {max(llist1):.2f}')
#             print(f'The minimum is {min(llist1):.2f}')
#             print(f'The average is {sum(llist1) / len(llist1):.2f}')
#         break  
#     llist1.append(float(score))
    



# -----------------------------------------------------------------------------



# 5

depth = int(input("What is the well's depth? "))
height = int(input("How high the frog can jump up? "))
slip = int(input("How far the frog slips down? "))


day = 1

meter_left = depth - height



while height != slip or depth == height:

    
    if meter_left > 0:
        print(f"On day {day} the frog leaps to the depth of {meter_left} meters.")

        meter_left = meter_left + slip
        print(f"At night he slips down to the depth of {meter_left} meters.") 
        meter_left = meter_left - height
        day += 1
    else:
        print(f"The frog is free on day {day}.")
        break
       
else:
    print(f"The frog will never escape from the well.")
    
        
        


       








