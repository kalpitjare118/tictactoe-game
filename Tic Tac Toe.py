import tkinter as tk
import random
from tkinter import messagebox

# Initialize variables
current_player = 'X'
board = [['' for _ in range(3)] for _ in range(3)]
player_mode = None

# Initialize scores
scores = {'X': 0, 'O': 0}

def reset_game():
    global current_player, board
    current_player = 'X'
    board = [['' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state='active')

def update_scores():
    scores_label.config(text=f"Scores: Player X: {scores['X']}  Player O: {scores['O']}")

# Create a Tkinter window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Set a custom background color for the window
window.configure(bg="#303030")

# Create buttons in a 3x3 grid
buttons = [[None, None, None] for _ in range(3)]

def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
    if empty_cells:
        i, j = random.choice(empty_cells)
        on_click(i, j)

def on_click(row, col):
    global current_player

    if board[row][col] == '' and current_player is not None:
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state='disabled')

        if check_winner(current_player):
            scores[current_player] += 1
            update_scores()
            if current_player == 'X':
                messagebox.showinfo("Tic-Tac-Toe", "Player 1 (X) wins!")
            else:
                if player_mode == 'Computer':
                    messagebox.showinfo("Tic-Tac-Toe", "Computer (O) wins!")
                else:
                    messagebox.showinfo("Tic-Tac-Toe", "Player 2 (O) wins!")
            current_player = None
        elif all(board[i][j] != '' for i in range(3) for j in range(3)):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            current_player = None
        else:
            current_player = 'X' if current_player == 'O' else 'O'
            if current_player == 'O' and player_mode == 'Computer':
                computer_move()

def set_mode(mode):
    global player_mode
    player_mode = mode

# Create buttons for mode selection
mode_frame = tk.Frame(window, bg="#303030")
mode_frame.grid(row=0, column=0, columnspan=3, pady=10)
mode_label = tk.Label(mode_frame, text="Select Mode:", fg="white", bg="#303030", font=('Arial', 14))
mode_label.grid(row=0, column=0, columnspan=3)
player_button = tk.Button(mode_frame, text="Player vs Player", command=lambda: set_mode("Player"), font=('Arial', 12))
player_button.grid(row=1, column=0)
computer_button = tk.Button(mode_frame, text="Player vs Computer", command=lambda: set_mode("Computer"), font=('Arial', 12))
computer_button.grid(row=1, column=1)

restart_button = tk.Button(window, text="Restart Game", command=reset_game, font=('Arial', 14), bg="#2980B9", fg="white", padx=20)
restart_button.grid(row=1, column=0, columnspan=3, pady=10)

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(window, text='', font=('Arial', 24), width=4, height=2, state='active', command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i + 2, column=j, padx=10, pady=10, ipadx=10, ipady=10)
        buttons[i][j].config(bg="#444444", fg="white", activebackground="#555555", activeforeground="white", relief=tk.SOLID, borderwidth=0)

scores_label = tk.Label(window, text="Scores: Player X: 0  Player O: 0", font=('Arial', 12), fg="white", bg="#303030")
scores_label.grid(row=4, column=0, columnspan=3, pady=10)

window.mainloop()
