water = 400
milk = 540
bean = 120
cup = 9
money = 550


def action():
    input_action = input('Write action(buy, fill, take):\n> ')
    return input_action

def buy():
    coffee = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: \n>  '))
    if coffee == 1:
        print('')
        print('The coffee machine has:')
        print(f'{water - 250} of water ')
        print(f'{milk} of milk')
        print(f'{bean - 16} of coffee beans ')
        print(f'{cup - 1} of disposable cups')
        print(f'{money + 4} of money')
    elif coffee == 2:
        print('')
        print('The coffee machine has:')
        print(f'{water - 350} of water ')
        print(f'{milk - 75} of milk')
        print(f'{bean - 20} of coffee beans ')
        print(f'{cup - 1} of disposable cups')
        print(f'{money + 7} of money')
    elif coffee == 3:
        print('')
        print('The coffee machine has:')
        print(f'{water - 200} of water ')
        print(f'{milk - 100} of milk')
        print(f'{bean - 12} of coffee beans ')
        print(f'{cup - 1} of disposable cups')
        print(f'{money + 6} of money')
    else: 
        print('')
        print('The coffee machine has:')
        print(f'{water} of water ')
        print(f'{milk} of milk')
        print(f'{bean} of coffee beans ')
        print(f'{cup} of disposable cups')
        print(f'{money} of money')
        pass


def fill():

    add_water = int(input('Write how many ml of water do you want to add: \n> '))
    add_milk = int(input('Write how many ml of milk do you want to add: \n> '))
    add_bean = int(input('Write how many grams of coffee beans do you want to add: \n> '))
    add_cup = int(input('Write how many disposable cups of coffee do you want to add: \n> '))

    print('')
    print('The coffee machine has:')
    print(f'{water + add_water} of water ')
    print(f'{milk + add_milk} of milk')
    print(f'{bean + add_bean} of coffee beans ')
    print(f'{cup + add_cup} of disposable cups')
    print(f'{money} of money')
    
def take():
    print(f'I gave you ${money}')

    print('')
    print('The coffee machine has:')
    print(f'{water} of water ')
    print(f'{milk} of milk')
    print(f'{bean} of coffee beans ')
    print(f'{cup} of disposable cups')
    print(f'{money - money} of money')

    


print('The coffee machine has:')
print(f'{water} of water ')
print(f'{milk} of milk')
print(f'{bean} of coffee beans ')
print(f'{cup} of disposable cups')
print(f'{money} of money')    
print('')
start = action()
if start == 'buy':
    buy()
elif start == 'fill':
    fill()
elif start == 'take':
    take()
else: pass