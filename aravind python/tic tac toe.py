import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title('Tic-Tac-Toe')

        self.current_player = 'X'
        self.board = [''] * 9
        self.win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
            (0, 4, 8), (2, 4, 6)            # Diagonals
        ]

        for i in range(9):
            row, col = divmod(i, 3)
            button = tk.Button(master, text='', font=('Arial', 60), width=2, height=1,
                               command=lambda i=i: self.click_button(i))
            button.grid(row=row, column=col)

    def click_button(self, i):
        button = self.master.grid_slaves()[i]
        if self.board[i] == '':
            button.configure(text=self.current_player)
            self.board[i] = self.current_player
            if self.check_win():
                self.show_win_message()
                self.reset_board()
            elif self.check_tie():
                self.show_tie_message()
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        for comb in self.win_combinations:
            if self.board[comb[0]] == self.board[comb[1]] == self.board[comb[2]] != '':
                return True
        return False

    def check_tie(self):
        return '' not in self.board

    def show_win_message(self):
        winner = self.current_player
        tk.messagebox.showinfo('Game Over', f'Player {winner} wins!')

    def show_tie_message(self):
        tk.messagebox.showinfo('Game Over', 'Tie game!')

    def reset_board(self):
        self.current_player = 'X'
        self.board = [''] * 9
        for button in self.master.grid_slaves():
            button.configure(text='')

root = tk.Tk()
app = TicTacToe(root)
root.mainloop()