import tkinter as tk
import random
from tkinter import messagebox

with open("words.txt", "r") as file: #update your own path
    words = [line.strip() for line in file.readlines()]


answer = random.choice(words)


root = tk.Tk()
root.title("Wordle Game")


window_width = 620
window_height = 420
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
root.resizable(False, False)


grid = [[tk.Label(root, width=4, height=2, borderwidth=1, relief="solid", font=("Helvetica", 18)) for _ in range(6)] for _ in range(6)]
for i in range(6):
    for j in range(5):
        grid[i][j].grid(row=i, column=j)


guessed_chars_label = tk.Label(root, text="  Guessed Characters", font=("Helvetica", 18))
guessed_chars_label.grid(row=0, column=6)


guessed_chars = tk.Label(root, text="", font=("Helvetica", 18))
guessed_chars.grid(row=1, column=6, rowspan=5)

guess_label= tk.Label(root, text="Guess:", font=("Helvetica", 18),)
guess_label.grid(row=7, column=0, columnspan=2, pady=20) 
entry = tk.Entry(root, font=("Helvetica", 15), width=8)
entry.grid(row=7, column=2, columnspan=2, pady=20)


def update_grid(guess, attempt):
    for i, char in enumerate(guess):
        if char == answer[i]:
            grid[attempt][i].config(text=char, bg="green")
        elif char in answer:
            grid[attempt][i].config(text=char, bg="yellow")
        else:
            grid[attempt][i].config(text=char, bg="red")
            guessed_chars.config(text=guessed_chars.cget("text") + char + " ")


def check_guess(event):
    guess = entry.get().strip().lower()
    if len(guess) == 5 and guess.isalpha() and guess in words:
        used_chars = guessed_chars.cget("text").replace(" ", "")
        if any(char in used_chars for char in guess):
            messagebox.showinfo("Invalid Guess", "You have used these characters already. They are marked in red.")
        else:
            update_grid(guess, check_guess.attempt)
            check_guess.attempt += 1
            entry.delete(0, tk.END)
            if guess == answer:
                entry.config(state="disabled")
                messagebox.showinfo("Congratulations", "You won!")
            elif check_guess.attempt==5:
                entry.config(state="disabled")
                messagebox.showinfo(":()", f"You lost! The correct word was {answer}")
    elif guess not in words:
        messagebox.showinfo("ERROR","Not a valid word")

check_guess.attempt = 0
entry.bind("<Return>", check_guess)

root.mainloop()
