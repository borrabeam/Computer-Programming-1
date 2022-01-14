import sys
water = 400
milk = 540
bean = 120
cup = 9
money = 550


def action():
    input_action = input('Write action (buy, fill, take, remaining, exit):\n> ')
    return input_action

def buy():
    global water,milk,bean,cup,money
    coffee = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n>  '))
    if coffee == 1:
        # print('')
        # print('The coffee machine has:')
        # print(f'{water - 250} of water ')
        # print(f'{milk} of milk')
        # print(f'{bean - 16} of coffee beans ')
        # print(f'{cup - 1} of disposable cups')
        # print(f'{money + 4} of money')
        if water >= 250 and bean >= 16 and cup >= 1:
            water = water - 250
            bean = bean - 16
            money = money + 4
            cup = cup - 1
            print("I have enough resources, making you a coffee!")
        elif water < 250:
            print("Sorry, not enough water!")
        elif bean < 16:
            print("Sorry, not enough coffee beans!")
        elif cup < 1:
            print("Sorry, not enough disposable cup!")

    elif coffee == 2:
        # print('')
        # print('The coffee machine has:')
        # print(f'{water - 350} of water ')
        # print(f'{milk - 75} of milk')
        # print(f'{bean - 20} of coffee beans ')
        # print(f'{cup - 1} of disposable cups')
        # print(f'{money + 7} of money')
        if water >= 350 and milk >= 75 and bean >= 20 and cup >= 1:
            water = water - 350
            milk = milk - 75
            bean = bean - 20
            money = money + 7
            cup = cup - 1
            print("I have enough resources, making you a coffee!")
        elif water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough coffee milk!")
        elif bean < 20:
            print("Sorry, not enough coffee beans!")
        elif cup < 1:
            print("Sorry, not enough disposable cup!")
    elif coffee == 3:
        # print('')
        # print('The coffee machine has:')
        # print(f'{water - 200} of water ')
        # print(f'{milk - 100} of milk')
        # print(f'{bean - 12} of coffee beans ')
        # print(f'{cup - 1} of disposable cups')
        # print(f'{money + 6} of money')
        if water >= 200 and milk >= 100 and bean >= 12 and cup >= 1:
            water = water - 200
            milk = milk - 100
            bean = bean - 12
            money = money + 6
            cup = cup - 1
            print("I have enough resources, making you a coffee!")
        elif water < 200:
            print("Sorry, not enough water!")
        elif milk < 100:
            print("Sorry, not enough coffee milk!")
        elif bean < 12:
            print("Sorry, not enough coffee beans!")
        elif cup < 1:
            print("Sorry, not enough disposable cup!")
    else: 
        # print('')
        # print('The coffee machine has:')
        # print(f'{water} of water ')
        # print(f'{milk} of milk')
        # print(f'{bean} of coffee beans ')
        # print(f'{cup} of disposable cups')
        # print(f'{money} of money')
        pass
    return water,milk,bean,cup,money

def fill():
    global water,milk,bean,cup
    add_water = int(input('Write how many ml of water do you want to add: \n> '))
    add_milk = int(input('Write how many ml of milk do you want to add: \n> '))
    add_bean = int(input('Write how many grams of coffee beans do you want to add: \n> '))
    add_cup = int(input('Write how many disposable cups of coffee do you want to add: \n> '))
    
    water = water + add_water
    milk = milk + add_milk
    bean = bean + add_bean
    cup = cup + add_cup

    print('')
    print('The coffee machine has:')
    print(f'{water} of water ')
    print(f'{milk} of milk')
    print(f'{bean} of coffee beans ')
    print(f'{cup} of disposable cups')
    print(f'{money} of money')
    return water,milk,bean,cup
    
def take():
    global money
    print(f'I gave you ${money}')
    money = money - money
    return money 
    # print('')
    # print('The coffee machine has:')
    # print(f'{water} of water ')
    # print(f'{milk} of milk')
    # print(f'{bean} of coffee beans ')
    # print(f'{cup} of disposable cups')
    # print(f'{money - money} of money')

def remaining():
    global water,milk,bean,cup,money
    print('')
    print('The coffee machine has:')
    print(f'{water} of water ')
    print(f'{milk} of milk')
    print(f'{bean} of coffee beans ')
    print(f'{cup} of disposable cups')
    print(f'{money} of money')
    return water,milk,bean,cup,money

# print('The coffee machine has:')
# print(f'{water} of water ')
# print(f'{milk} of milk')
# print(f'{bean} of coffee beans ')
# print(f'{cup} of disposable cups')
# print(f'{money} of money')    
# print('')

while True:
    start = action()
    if start == 'buy':
        buy()
    elif start == 'fill':
        fill()
    elif start == 'take':
        take()
    elif start == 'remaining':
        remaining()
    elif start == 'exit':
        sys.exit()
    else: pass