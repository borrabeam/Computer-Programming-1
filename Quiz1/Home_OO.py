class Home:
    def __init__(self,device,watt,status):
        self.__device = device
        self.__watt = watt
        self.__status = status
        
    def __str__(self):
        return '{0} {1} Watts is {2}'.format(self.__device,self.__watt,self.__status)

    @property
    def device(self):
        return self.__device
    @device.setter
    def device(self,name):
        self.__device = name

    @property
    def watt(self):
        return self.__watt
    @watt.setter
    def model(self,name):
        self.__watt = name

    @property
    def status(self):
        return self.__status
    @status.setter
    def price(self,name):
        self.__status = name

home_list = []

def menu():
    choice = input('(a)dd device, (s)how device, (q)uit: ')
    while choice != 'q':
    
        if choice == 'a':
            device = input('Device name: ')
            watt = int(input('Watt: '))
            status = input('On or Off? : ')
            home_list.append(Home(device,watt,status))
            choice = input('(a)dd device, (s)how device, (q)uit: ')
        elif choice == 's':
            for i in home_list:
                print(i)
            choice = input('(a)dd device, (s)how device, (q)uit: ')
        else: choice = input('(a)dd device, (s)how device, (q)uit: ')
    print('Bye')


menu()