import time
def current_time():
    return time.time()
    

while True:
    menu = input('(s)tart,(e)lapse,(q)uit: ')
    if menu == 's':
        start = current_time()
    elif menu =='e':
        elapse = current_time() - start
        print(f'{elapse:.0f}seconds')
    elif menu =='q':
        stop = current_time()
        deiffernce = int(stop - start)
        print(f'Total {deiffernce} seconds')s
        break
    else:
        print('Incorrect Menu')



