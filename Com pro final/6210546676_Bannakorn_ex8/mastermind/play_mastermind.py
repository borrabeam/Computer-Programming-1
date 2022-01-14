from mastermind import * 

new_game = MasterMindBoard()
while (True):
    input_guess = input("What is your guess?: ")
    print('Your guess is', input_guess)
    a = new_game.guess12(input_guess)
    new_game.display_clue(input_guess)
    if new_game.done(a):
        break
