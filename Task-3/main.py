from tkinter import *
import random

root = Tk()
root.geometry("500x400")
bg = "#0077b6"
fg = "white"
# --------------Logic------------#
choices = ["Rock", "Paper", "Scissor"]


def play(choice):
    idea.destroy()
    computer = random.choice(choices)
    computer_choice.config(text=computer)
    user_choice.config(text=choice)
    print(computer)
    if choice == "Rock" and computer == "Paper" :
        result_label.config(text="You Loose.!")
    elif choice == "Paper" and computer == "Scissor":
        result_label.config(text="You Loose.!")
    elif choice == "Scissor" and computer == "Rock":
        result_label.config(text="You Loose.!")
    elif (choice == "Scissor" and computer == "Scissor") or (choice == "Rock" and computer == "Rock") or (choice == "Paper" and computer == "Paper"):
        result_label.config(text="Match Tied")
    else:
        result_label.config(text="You Win.!")
        
# -------------UI-------------#
Label(
    text="Your Choice  ", highlightthickness=0, bd=0, font=("arial", 15, "italic")
).place(x=50, y=20)

user_choice = Label(
    root,
    text="",
    font=("arial", 15, "italic"),
)
user_choice.place(x=400, y=20)


Label(
    root,
    text="Computer Choice  ",
    highlightthickness=0,
    bd=0,
    font=("arial", 15, "italic"),
).place(x=50, y=80)

computer_choice = Label(
    text="",
    font=("arial", 15, "italic"),
)
computer_choice.place(x=400, y=80)
#IDea
idea = Label(text="Choose Button to play",font=("arial", 12, "italic"))
idea.place(x=160,y=180)
# Buttons

rock_btn = Button(
    text="Rock",
    width=7,
    font=("arial", 15, "italic"),
    bg=bg,
    fg=fg,
    highlightthickness=0,
    command=lambda: play("Rock"),
).place(x=50, y=220)

paper_btn = Button(
    text="Paper",
    width=7,
    font=("arial", 15, "italic"),
    bg=bg,
    fg=fg,
    highlightthickness=0,
    command=lambda: play("Paper"),
).place(x=190, y=220)

scissor_btn = Button(
    text="Scissor",
    width=7,
    font=("arial", 15, "italic"),
    bg=bg,
    fg=fg,
    highlightthickness=0,
    command=lambda: play("Scissor"),
).place(x=320, y=220)


# Win/Loose
result_label = Label(
    text="", highlightthickness=0, bd=0, font=("arial", 20, "italic")
)
result_label.place(x=180, y=300)

root.mainloop()
