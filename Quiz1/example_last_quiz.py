import time

class Route:
    def __init__(self,route_name):
        self.__route_name = route_name
        self.__bus_list = []
    
    def __str__(self):
        return self.__route_name

    def add_bus(self, new_bus):
        self.__bus_list.append(new_bus)

    def print_route(self):
        for i in range(len(self.__bus_list)):
            print(f"{i+1}.{self.__bus_list[i]}")

    def get_bus(self, choose):
        return self.__bus_list[choose-1]

    @property
    def route(self):
        return self.__route_name
    @route.setter
    def route(self,route):
        self.__route_name = route

class Bus:
    def __init__(self,bus_code):
        self.__bus_code = bus_code
        self.__start_time = 0
        self.__status = "Stop"
        self.__total_time = 0
    
    def __str__(self):
        if self.status == "Stop":
            elaspe = 0
        else:
            elaspe = time.time() - self.start_time
        return f"{self.__bus_code} is {self.status} (Current {elaspe:.0f} secs / All {self.total_time:.0f} secs)"

    @property 
    def total_time(self):
        return self.__total_time
    @total_time.setter
    def total_time(self, value):
        self.__total_time = value

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,status):
        self.__status = status

    @property
    def start_time(self):
        return self.__start_time
    @start_time.setter
    def start_time(self,start_time):
        self.__start_time = start_time

class App():
    
    def __init__(self):
        self.list_route = [0]
    
    def add_route(self, route_name):
        new_route = Route(route_name)
        self.list_route.append(new_route)
        self.show_route()

    def show_route(self):
        for i in range(len(self.list_route)):
            print(f"Route {i+1}: {self.list_route[i].route}")    

    def choose_route(self, num_route):
        # Minus 1 to choose position in the list
        route_choose = self.list_route[num_route-1]
        sub_menu = input("(a)dd bus, (p)rint, (r)un/stop, (m)ain menu: ").lower()
        while sub_menu != 'm':
            if sub_menu == 'a':
                bus_code = input("Bus Code: ")
                bus = Bus(bus_code)
                route_choose.add_bus(bus)
            if sub_menu == 'r':
                bus_number = int(input("Bus Number? : "))
                choosed_bus = route_choose.get_bus(bus_number)
                if(choosed_bus.status == "Stop"):
                    choosed_bus.status = 'Running'
                    choosed_bus.start_time = time.time()
                else:
                    choosed_bus.status = "Stop"
                    choosed_bus.total_time += (time.time() - choosed_bus.start_time)

                print(f"Route {num_route}: {route_choose}")
                route_choose.print_route()
            if sub_menu == "p" :
                print(f"Route {num_route}: {route_choose}")
                route_choose.print_route()


            sub_menu = input("(a)dd bus, (p)rint, (r)un/stop, (m)ain menu: ")
    

app = App()
menu = input("(n)ew Route,(s)how,(c)hoose,(q)uit: ").lower()
while menu != "q":
    if menu == "n":
        route_name = input("Enter route name: ")
        app.add_route(route_name)
        menu = input("(n)ew Route,(s)how,(c)hoose,(q)uit: ").lower()
    elif menu == "s":
        app.show_route()
    elif menu == "c":
        num_route = int(input("Enter a route number: "))
        app.choose_route(num_route)
        
    else:
        print("invalid")
    
