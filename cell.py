from tkinter import *
import settings
import ctypes


class Cell:
    turn = 0
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]
    win_combinations = settings.WIN

    def __init__(self, x, y):
        self.cell_btn_object = None
        self.x = x
        self.y = y


    def create_btn_object(self, location):
        btn = Button(
            location,
            width=10,
            height=5,
            font=30
        )
        btn.bind('<Button-1>', self.left_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if Cell.turn % 2 != 0:
            self.show_x()
            Cell.turn += 1
        else:
            self.show_0()
            Cell.turn += 1
        self.cell_btn_object.unbind('<Button-1>')
        self.tictactoe_win_check()

    def show_x(self):
        self.cell_btn_object.configure(
            text='X'
        )
        Cell.board[self.x][self.y] = 'X'

    def show_0(self):
        self.cell_btn_object.configure(
            text='0'
        )
        Cell.board[self.x][self.y] = '0'

    @staticmethod
    def tictactoe_win_check():
        for indices in Cell.win_combinations:
            row = [Cell.board[r][c] for r, c in indices]
            if all(cell == 'X' for cell in row):
                ctypes.windll.user32.MessageBoxW(0, 'X player wins!', 'Game Finished', 0)
            elif all(cell == '0' for cell in row):
                ctypes.windll.user32.MessageBoxW(0, '0 player wins!', 'Game Finished', 0)
            elif Cell.turn == 9:
                ctypes.windll.user32.MessageBoxW(0, 'Draw!', 'Game Finished', 0)
                break
        return None

    def __repr__(self):
        return repr(self.x), repr(self.y)
