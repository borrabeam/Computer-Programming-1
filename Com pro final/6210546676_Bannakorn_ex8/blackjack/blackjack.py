from deck import *


class Blackjack:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = []
        self.computer_hand = []
        self.player_hand_value = 0
        self.computer_hand_value = 0
        # [stay or dead or can_stay or must_draw_more]
        self.player_hand_status = ''
        # [stay or dead or can_stay or must_draw_more]
        self.computer_hand_status = ''

    def start(self):
        self.player_hand = self.deck.draw_card(2)
        self.computer_hand = self.deck.draw_card(2)

    def adjust_player_hand(self):
        self.player_hand.extend(self.deck.draw_card(1))
        self.check_player()

    def adjust_computer_hand(self):
        self.computer_hand.extend(self.deck.draw_card(1))
        self.check_computer()

    def display_player_hand(self):
        print('Player hand')
        print(self.player_hand)

    def display_computer_hand(self):
        print('Computer hand')
        print(self.computer_hand)

    def decision(self):
        if self.computer_hand_value == self.player_hand_value:
            print('Both ties')
        elif self.player_hand_status == 'win':
            print('Player win!')
        elif self.computer_hand_status == 'win':
            print('Computer win!')

    def check_player(self):
        self.player_hand_value = 0
        for i in range(len(self.player_hand)):
            sp = self.player_hand[i].split()
            if sp[0] == 'Jack' or sp[0] == 'Queen' or sp[0] == 'King':
                sp[0] = 10
            elif sp[0] == 'Ace':
                if (self.player_hand_value + 11) > 21:
                    sp[0] = 1
                else:
                    sp[0] = 11

            self.player_hand_value += int(sp[0])
            # print(self.player_hand_value)
            if 16 <= self.player_hand_value <= 21:
                self.player_hand_status = 'can_stay'
            if self.player_hand_value == 21:
                self.player_hand_status = 'win'
            elif self.player_hand_value > 21:
                self.computer_hand_status = 'win'

    def check_computer(self):
        self.computer_hand_value = 0
        for i in range(len(self.computer_hand)):
            sp = self.computer_hand[i].split()
            if sp[0] == 'Jack' or sp[0] == 'Queen' or sp[0] == 'King':
                sp[0] = 10
            elif sp[0] == 'Ace':
                if (self.computer_hand_value + 11) > 21:
                    sp[0] = 1
                else:
                    sp[0] = 11

            self.computer_hand_value += int(sp[0])
            if 16 <= self.computer_hand_value <= 21 and self.computer_hand_value > self.player_hand_value:
                self.computer_hand_status = 'can_stay'
            if self.computer_hand_value == 21:
                self.computer_hand_status = 'win'
            elif self.player_hand_value > 21:
                self.computer_hand_status = 'win'
            elif self.computer_hand_value > 21:
                self.player_hand_status = 'win'
            elif self.computer_hand_value < self.player_hand_value:
                self.player_hand_status = 'win'
            elif self.computer_hand_value > self.player_hand_value:
                self.computer_hand_status = 'win'
