class Route:



    def __init__(self,route):
        self.__route = route
        self.__route_list = route_list
        
    def __str__(self):
        # for i in range(len(self.__route_list)):
            # a = f'Route {i+1}: {self.__route}'
        return  f'Route: {self.__route}'

    @property
    def route(self):
        return self.__route
    @route.setter
    def device(self,name):
        self.__route = name


class Bus:
    def __init__(self,bus):
        self.__bus = bus
        

    def __str__(self):
        return  f' {self.__bus}'


route_list = []
bus_code_list = []

def menu():
    choice = input('(n)ew Route,(s)how,(c)hoose,(q)uit ')
    while choice != 'q':
    
        if choice == 'n':
            route = input('Enter route name: ')
            route_list.append(Route(route))
            choice = input('(n)ew Route,(s)how,(c)hoose,(q)uit: ')
        elif choice == 's':
            for i in route_list:
                print(i)
            choice = input('(n)ew Route,(s)how,(c)hoose,(q)uit: ')
        elif choice == 'c':
            route_num = int(input('Enter a route number: '))
            
            choice2 = input('(a)dd bus,(p)rint,(r)un/stop,(m)ain menu: ')
            if choice2 == 'a':
                bus_code = input('Bus Code:')
                bus_code_list.append(Bus(bus_code))
                # choice2 = input('(a)dd bus,(p)rint,(r)un/stop,(m)ain menu: ')
            elif choice2 == 'p':
                print(route_list[route_num - 1])
                for i in bus_code_list:
                    print(i)
                # choice2 = input('(a)dd bus,(p)rint,(r)un/stop,(m)ain menu: ')
            elif choice2 == 'r':
                pass
            elif choice2 == 'm':
                choice = input('(n)ew Route,(s)how,(c)hoose,(q)uit: ')
            else: choice2 = input('(a)dd bus,(p)rint,(r)un/stop,(m)ain menu: ')

        else: choice = input('(n)ew Route,(s)how,(c)hoose,(q)uit ')
    print('Bye :(')


menu()






