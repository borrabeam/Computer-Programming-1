import random


class MasterMindBoard:

    def __init__(self):

        str1 = ''
        for i in range(4):
            str1 += str(random.randint(1, 6))
            self.solution = str1
            self.num_guess = 0
            self.guess = ''
            self.clue = ''

    def guess12(self, input_guess):

        if self.solution != input_guess:
            self.guess = ''
            self.num_guess += 1

            # correct = '*'
            # incorrect_po = 'O'

            self.solution = list(self.solution)
            input_guess = list(input_guess)
            
            for i in range(0,4):
                if input_guess[i] == self.solution[i]:
                    # input_guess[i] = correct
                    # self.guess += correct
                    input_guess[i] = "*"
                    

                elif input_guess[i] in self.solution:
                    input_guess[i] = "O"
                    # input_guess = input_guess[:i] + incorrect_po + input_guess[i+1:]
                else:
                    input_guess[i] = " "
                    # input_guess = input_guess[:i] + '' + input_guess[i+1:]
            input_guess = ''.join(input_guess)
                    
        print(f'{input_guess}')
        return input_guess

    def display_clue(self,input_guess):
        self.solution = list(self.solution)
        input_guess = list(input_guess)

        for i in range(0,4):
            if self.solution[i] > input_guess[i]:
                print(f'{i} Higher')
            elif self.solution[i] < input_guess[i]:
                print(f'{i} Lower')

    def done(self,input_guess):
        if input_guess == '****' :
            print(f'You solve it after {self.num_guess} rounds')
            return True


