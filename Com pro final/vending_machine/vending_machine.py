class VendingMachine:
    """A vending machine that vends some product for some price.
    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Inventory empty. Restocking required.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Inventory empty. Restocking required. Here is your $15.'
    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, item, price):
        # item is of str type
        self.item = item
        # price is of int type
        self.price = price
        self.available_fund = 0
        self.available_item = 0
    
    def add_funds(self, fund):
        # this method increases the available fund
        # can only add fund if inventory not empty; otherwise return fund
        if self.available_item > 0:
            self.available_fund += fund
            return 'Current balance: $' +  str(self.available_fund)
        else:
            return 'Inventory empty. Restocking required. Here is your $' + str(fund) +'.'

    def restock(self, num_restock):
        # this method increase the available item
        self.available_item += num_restock
        return 'Current ' + str(self.item) + ' stock: ' + str(self.available_item)

    def vend(self):
        # can vend when 1.available_fund > price 2. available_item > 0
        # when vend: 1. return available_fund - price as change
        if self.available_item > 0:
            if self.available_fund > self.price:
                change = self.available_fund - self.price
                self.available_fund = 0
                self.available_item -= 1
                return 'Here is your ' + str(self.item) + ' and $' + str(change) + ' change.'

            elif self.available_fund < self.price:
                return "You must add $" +  str(self.price - self.available_fund) + " more funds."

            else:
                self.available_fund = 0
                self.available_item -= 1
                return 'Here is your ' + str(self.item) + '.'
        else:
            return 'Inventory empty. Restocking required.'