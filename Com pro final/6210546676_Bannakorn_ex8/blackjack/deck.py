class Deck:
    def __init__(self):
        suits = ['\u2663', '\u2666', '\u2660', '\u2665']
        ranks = ['2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = []
        for rank in ranks:
            for suit in suits:
                card = rank + ' ' + suit
                deck += [card]
        self.card_deck = deck

    def shuffle(self):
        import random
        n = len(self.card_deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = self.card_deck[r]
            self.card_deck[r] = self.card_deck[i]
            self.card_deck[i] = temp

    def str(self):

        card_str = ""
        for card in self.card_deck:
            card_str += card + ','
        return card_str[:-1]

    def draw_card(self,n):
        hand = []
        for i in range(n):
            hand.append(self.card_deck.pop(i))
        return hand
  