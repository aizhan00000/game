
import subprocess as sp


class Game:
    def __init__(self):
        self.choices = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ]

    def print_arena(self):
        print("%s | %s | %s" % (self.choices[1], self.choices[2], self.choices[3]))
        print("----------")
        print("%s | %s | %s" % (self.choices[4], self.choices[5], self.choices[6]))
        print("----------")
        print("%s | %s | %s" % (self.choices[7], self.choices[8], self.choices[9]))

    def save_choice(self, value, index):
        if self.choices[index] == ' ':
            self.choices[index] = value

    def win(self, value):
        if (self.choices[1] == value and  self.choices[2] == value and self.choices[3] == value)\
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
    sp.call


def refresh():
    sp.call('clear', shell=True)
    print("Game: Tic-TAc-TOe")
    game.print_arena()


def update_cell(self, cell, value):
    if self.cells[cell] == ' ':
        self.cells[cell] == value
    else:
        while True:
            cell = int(input("enter another cell:  "))
            if self.cells[cell] == ' ':
                self.cells[cell] == value
                break


def play_again():
    again = input("do you want to play again?(y/n)").lower()
    if again == 'y':
        game.clear_cells()
        return True
    else:
        return False



while True:
    refresh()
    x = int(input("enter cell from 1-9 to place X :  "))
    game.save_choice('X', x)
    if game.win('X'):
        print("X is wins")
        if play_again():
            continue
        else:
            break
    o = int(input("enter cell from 1 to 9 to place O:  "))
    game.save_choice('O', o)
    refresh()
    if game.win('O'):
        print("O WINS!!!")
        if play_again():
            continue
        else:
            break





