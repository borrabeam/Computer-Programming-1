import random


word_list = ['java', 'python', 'javascript', 'kotlin']
life = 8


def get_random_word(lst):
    return random.choice(lst)


secret = get_random_word(word_list)
secret_list = list(secret)
guessed_list = list("-" * len(secret))
gussed_letter_list = []

print('H A N G M A N')
print(''.join(guessed_list))
while True:
    if life == 0:
        print('You are hanged!')
        break
    if guessed_list == secret_list:
        print('You get the word!')
        print('You survived!')
        break
    guess_letter = input('Input a letter: > ')
    if guess_letter in secret_list:
        if guess_letter in gussed_letter_list:
            print('No improvements')
            life -= 1
        else:
            for i in range(len(secret_list)):
                if guess_letter == secret_list[i]:
                    guessed_list[i] = guess_letter
                    gussed_letter_list.append(guess_letter)
            print(''.join(guessed_list))
    else:
        print('No such letter in the word')
        life -= 1