import tkinter as tk
import random

# Main window setup
app = tk.Tk()
app.title("RPS Game")
app.geometry("400x400")
app.configure(bg="#e6f2ff")

# Scores
player_points = 0
cpu_points = 0

# Get random choice for computer
def cpu_choice():
    return random.choice(['rock', 'paper', 'scissor'])

# Decide winner
def check_winner(player, cpu):
    if player == cpu:
        return 'draw'
    elif (player == 'rock' and cpu == 'scissor') or \
         (player == 'paper' and cpu == 'rock') or \
         (player == 'scissor' and cpu == 'paper'):
        return 'player'
    else:
        return 'cpu'

# Main game function
def make_move(choice):
    global player_points, cpu_points

    cpu = cpu_choice()
    result = check_winner(choice, cpu)

    msg = f"You picked: {choice}\nComputer picked: {cpu}\n"

    if result == 'draw':
        msg += "It's a draw."
    elif result == 'player':
        player_points += 1
        msg += "You won this round! 🎉"
    else:
        cpu_points += 1
        msg += "Computer won this round. 🤖"

    status_label.config(text=msg)
    score_label.config(text=f"Scores — You: {player_points} | CPU: {cpu_points}")

# Reset function
def restart_game():
    global player_points, cpu_points
    player_points = 0
    cpu_points = 0
    status_label.config(text="Choose Rock, Paper, or Scissor to start!")
    score_label.config(text="Scores — You: 0 | CPU: 0")

# GUI Elements
header = tk.Label(app, text="🎮 Rock-Paper-Scissor Game 🎮", font=("Verdana", 14, "bold"), bg="#e6f2ff")
header.pack(pady=12)

status_label = tk.Label(app, text="Choose Rock, Paper, or Scissor to start!", font=("Arial", 12), bg="#e6f2ff")
status_label.pack(pady=15)

buttons = tk.Frame(app, bg="#e6f2ff")
buttons.pack()

btn_rock = tk.Button(buttons, text="Rock", width=12, command=lambda: make_move('rock'))
btn_paper = tk.Button(buttons, text="Paper", width=12, command=lambda: make_move('paper'))
btn_scissor = tk.Button(buttons, text="Scissor", width=12, command=lambda: make_move('scissor'))

btn_rock.grid(row=0, column=0, padx=8, pady=5)
btn_paper.grid(row=0, column=1, padx=8, pady=5)
btn_scissor.grid(row=0, column=2, padx=8, pady=5)

score_label = tk.Label(app, text="Scores — You: 0 | CPU: 0", font=("Helvetica", 12), bg="#e6f2ff")
score_label.pack(pady=20)

reset_btn = tk.Button(app, text="Start Over", command=restart_game)
reset_btn.pack(pady=10)

# Start GUI loop
app.mainloop()
