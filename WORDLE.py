import tkinter as tk
import random
from tkinter import messagebox

with open("words.txt", "r") as file: #update your own path
    words = [line.strip() for line in file.readlines()]


answer = random.choice(words)
guessed_char=[]


root = tk.Tk()
root.title("Wordle Game")


window_width = 620
window_height = 440
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


guessed_chars_label = tk.Label(root, text=" Guessed Characters", font=("Helvetica", 18))
guessed_chars_label.grid(row=0, column=5)


guessed_chars = tk.Label(root, text="", font=("Helvetica", 18))
guessed_chars.grid(row=1, column=5, rowspan=5)

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
            if char not in guessed_char:
                guessed_chars.config(text=guessed_chars.cget("text") + char + " ")
                guessed_char.append(char)


def check_guess(event):
    guess = entry.get().strip().lower()
    if len(guess) == 5 and guess.isalpha() and guess in words:
        update_grid(guess, check_guess.attempt)
        check_guess.attempt += 1
        entry.delete(0, tk.END)
        if guess == answer:
            entry.config(state="disabled")
            messagebox.showinfo("Congratulations", "You won!")
            exit()
        elif check_guess.attempt==6:
            entry.config(state="disabled")
            messagebox.showinfo(":()", f"You lost! The correct word was {answer}")
            exit()
    elif guess not in words:
        messagebox.showwarning("ERROR","Not a valid word")
    elif not guess.isalpha():
        messagebox.showwarning("ERROR! Invalid characters in word")

def forfeit():
    entry.config(state="disabled")
    messagebox.showinfo(":()", f"You lost! The correct word was {answer}")
    exit()


button = tk.Button(root, 
                   text="Forfeit", 
                   command=forfeit,
                   activebackground="blue", 
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="gray",
                   fg="black",
                   font=("Arial", 12),
                   height=1,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=1,
                   justify="center",
                   overrelief="raised",
                   padx=10,
                   pady=5,
                   width=12,
                   wraplength=100)


button.grid(row=7, column=5)


check_guess.attempt = 0
entry.bind("<Return>", check_guess)

root.mainloop()