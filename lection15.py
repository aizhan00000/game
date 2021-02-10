import subprocess as sp


class Game:
    def __init__(self):
        self.choices = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]

    def print_arena(self):
        print("%s | %s | %s" % (self.choices[1], self.choices[2], self.choices[3]))
        print("----------")
        print("%s | %s | %s" % (self.choices[4], self.choices[5], self.choices[6]))
        print("----------")
        print("%s | %s | %s" % (self.choices[7], self.choices[8], self.choices[9]))

    def save_choice(self, value, index):
        if self.choices[index] == ' ':
            self.choices[index] = value
        else:
            while True:
                choice = int(input("enter another choice:  "))
                if self.choices[choice] == ' ':
                    self.choices[choice] = value
                    break

    def is_winner(self, value):
        compare = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for i in compare:
            for j in i:
                if self.cells[j] != value:
                    result = False
            if result:
                return True

        return False

    def is_tie(self):
        filled_choices = 0
        for i in self.choices:
            if i != ' ':
                filled_choices += 1
                if filled_choices == 9:
                    return True
                else:
                    return False

    def ai_move(self, value):
        if self.choices[5] == value:
            self.save_choice(5, value)

        for i in range(1, 10):
            if self.choices[i] == ' ':




    def win(self, value):
        if (self.choices[1] == value and self.choices[2] == value and self.choices[3] == value)\
            or (self.choices[4] == value and self.choices[5] == value and self.choices[6] == value)\
            or (self.choices[1] == value and self.choices[6] == value and self.choices[9] == value)\
            or (self.choices[3] == value and self.choices[5] == value and self.choices[7] == value)\
            or (self.choices[1] == value and self.choices[4] == value and self.choices[7] == value)\
            or (self.choices[2] == value and self.choices[5] == value and self.choices[8] == value)\
                or (self.choices[3] == value and self.choices[6] == value and self.choices[9] == value):
            return True

    def clear_cells(self):
        self.choices = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]


game = Game()
game.print_arena()


def refresh():
    sp.call('clear', shell=True)
    print("Game: Tic-TAc-TOe")
    game.print_arena()


def play_again():
    again = input("do you want to play again?(y/n)").lower()
    if again == 'y':
        game.clear_cells()
        return True
    else:
        print("see you!!!")


while True:
    refresh()
    x = int(input("enter cell from 1-9 to place X :  "))
    game.save_choice('X', x)
    if game.win('X'):
        print("X is wins")
        print("O lost")
        if play_again():
            continue
        else:
            break
    o = int(input("enter cell from 1 to 9 to place O:  "))
    game.save_choice('O', o)
    refresh()
    if game.win('O'):
        print("O WINS!!!")
        print("X lost")
        if play_again():
            continue
        else:
            break








