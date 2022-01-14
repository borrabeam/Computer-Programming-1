from Multiple_blackjack import *
from deck import *

new_bj_game = Blackjack()
new_bj_game.multiple_player()
new_bj_game.start()

new_bj_game.display_computer_hand()
new_bj_game.check_computer()

new_bj_game.display_player_hand()
new_bj_game.check_player()

# player

while (new_bj_game.player_hand_status != 'can_stay'):
    print(new_bj_game.player_hand_value)
    if new_bj_game.player_hand_value >= 21:
        break
    else:
        new_bj_game.adjust_player_hand()
        new_bj_game.display_player_hand()

while(new_bj_game.player_hand_status == 'can_stay' and new_bj_game.player_hand_value < 21):
    print(new_bj_game.player_hand_value)
    to_stay_or_not = input('stay or not: ')
    if to_stay_or_not == 'stay' :
        break
    else:
        new_bj_game.adjust_player_hand()
        new_bj_game.display_player_hand()


while (new_bj_game.computer_hand_status != 'can_stay' and new_bj_game.player_hand_value <= 21):
    print(new_bj_game.computer_hand_value)
    if new_bj_game.computer_hand_status == 'can_stay' or new_bj_game.computer_hand_value > 21 or new_bj_game.computer_hand_value > new_bj_game.player_hand_value:
        break
    else:
        new_bj_game.adjust_computer_hand()
        new_bj_game.display_computer_hand()
# else:
#         new_bj_game.adjust_computer_hand()
#         new_bj_game.display_computer_hand()

new_bj_game.decision()
