class Route:
    def __init__(self,route_name):
        self.__route_name = route_name

    @property
    def get_route_name(self):
        return self.__route_name
    @get_route_name.setter
    def set_route_name(self,name):
        self.__route_name = name

class Bus:
    def __init__(self,bus):
        self.__bus = bus
        self._route = Route

    @property
    def get_bus(self):
        return self.__bus
    @get_bus.setter
    def set_bus(self,name):
        self.__bus = name


route_list = []
bus_code_list = []

def menu():
    first_menu = input('(n)ew Route,(s)how,(c)hoose,(q)uit ')
    while first_menu != 'q':
        if first_menu == 'n':
            input_route_name = input('Enter route name : ')
            route_list.append(input_route_name)
            for i in range(len(route_list)):
                print(f'Route {i+1} : {route_list[i]}')
            first_menu = input('(n)ew Route,(s)how,(c)hoose,(q)uit ')
        elif first_menu == 's':
            for i in range(len(route_list)):
                print(f'Route {i+1} : {route_list[i]}')
        elif first_menu == 'c':
            input_route_number = int(input('Enter a route number: '))
            class_selected = 
            second_menu = input('(a)dd bus,(p)rint,(r)un/stop,(m)ain menu: ')



menu()