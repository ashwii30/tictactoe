import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        self.player = 'X'
        self.score = {'X': 0, 'O': 0}
        self.board = [None] * 9
        self.buttons = [tk.Button(root, text='', font='Arial 40 bold', width=5, height=2,
                                  command=lambda i=i: self.on_click(i)) for i in range(9)]
        
        self.create_board()
        self.create_scoreboard()
        self.create_restart_button()
        self.update_turn_indicator()

    def create_board(self):
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col, sticky="nsew")
        
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def create_scoreboard(self):
        self.score_label = tk.Label(self.root, text=self.get_score_text(), font='Arial 20 bold')
        self.score_label.grid(row=3, column=0, columnspan=3)
        
    def get_score_text(self):
        return f"Score \n X: {self.score['X']}  O: {self.score['O']}"

    def create_restart_button(self):
        self.restart_button = tk.Button(self.root, text="Restart Game", font='Arial 20 bold', command=self.reset_board)
        self.restart_button.grid(row=4, column=0, columnspan=3, pady=20)

    def update_turn_indicator(self):
        self.turn_indicator = tk.Label(self.root, text=f"Turn: Player {self.player}", font='Arial 20 bold')
        self.turn_indicator.grid(row=5, column=0, columnspan=3)

    def on_click(self, index):
        if self.board[index] is None:
            self.board[index] = self.player
            self.buttons[index].config(text=self.player, fg='red' if self.player == 'X' else 'blue')
            if self.check_winner():
                self.highlight_winner()
                self.score[self.player] += 1
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player} wins!")
                self.update_score()
                self.reset_board()
            elif None not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.update_turn_indicator()

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == self.player:
                self.winning_combo = combo
                return True
        return False

    def highlight_winner(self):
        for index in self.winning_combo:
            self.buttons[index].config(bg='yellow')

    def reset_board(self):
        self.board = [None] * 9
        for button in self.buttons:
            button.config(text='', bg='SystemButtonFace')
        self.winning_combo = []
        self.player = 'X'
        self.update_turn_indicator()

    def update_score(self):
        self.score_label.config(text=self.get_score_text())

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
