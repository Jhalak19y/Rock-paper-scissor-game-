from tkinter import *
from PIL import Image, ImageTk
import random

# Initialize Tkinter window
window = Tk()
window.title("Rock Paper Scissor")
window.geometry("800x680")

# Load images for player and computer choices
rock_img = ImageTk.PhotoImage(Image.open("rock.png.jpg").resize((200, 200)))
paper_img = ImageTk.PhotoImage(Image.open("paper.jpg").resize((200, 200)))
scissor_img = ImageTk.PhotoImage(Image.open("scissor.jpeg").resize((200, 200)))

# Dictionary to map choices to images
image_dict = {
    "rock": rock_img,
    "paper": paper_img,
    "scissor": scissor_img,
}

# Initialize game variables
player_score = 0
computer_score = 0
round_count = 0
max_rounds = 5

# Function to play the game
def play_game(player_choice):
    global player_score, computer_score, round_count

    if round_count < max_rounds:
        computer_choice = random.choice(["rock", "paper", "scissor"])
        result = determine_winner(player_choice, computer_choice)

        # Display player and computer choices
        player_label.config(image=image_dict[player_choice])
        computer_label.config(image=image_dict[computer_choice])

        # Update scores and round count
        if result == "You Win":
            player_score += 1
        elif result == "Computer Wins":
            computer_score += 1
        round_count += 1

        # Display result
        result_label.config(text=f"Round {round_count}: {result}")

        if round_count == max_rounds:
            display_final_result()
    else:
        result_label.config(text="Game Over")

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "Draw"
    elif (player == "rock" and computer == "scissor") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissor" and computer == "paper"):
        return "You Win"
    else:
        return "Computer Wins"

# Function to reset the game
def reset_game():
    global player_score, computer_score, round_count
    player_score = 0
    computer_score = 0
    round_count = 0
    player_label.config(image='')
    computer_label.config(image='')
    result_label.config(text="")
    reset_button.pack_forget()

# Function to display the final result
def display_final_result():
    if player_score > computer_score:
        final_result = "You are the overall winner!"
    elif player_score < computer_score:
        final_result = "Computer is the overall winner!"
    else:
        final_result = "It's a tie!"

    result_label.config(text=f"{final_result}\nFinal Score: You {player_score} - {computer_score} Computer")
    reset_button.pack(pady=20)

# Create GUI elements
Label(window, text="Rock Paper Scissor", font=("Algerian", 30)).pack(pady=20)

# Frame for labels
label_frame = Frame(window)
label_frame.pack()

player_label = Label(label_frame, text="Player", font=("Algerian", 20))
player_label.pack(side=LEFT, padx=20)

Label(label_frame, text="VS", font=("Algerian", 30)).pack(side=LEFT)

computer_label = Label(label_frame, text="Computer", font=("Algerian", 20))
computer_label.pack()

# Result label
result_label = Label(window, text="", font=("Algerian", 25))
result_label.pack(pady=20)

# Frame for buttons
button_frame = Frame(window)
button_frame.pack()

# Buttons for player choices
Button(button_frame, image=rock_img, command=lambda: play_game("rock")).pack(side=LEFT, padx=20)
Button(button_frame, image=paper_img, command=lambda: play_game("paper")).pack(side=LEFT, padx=20)
Button(button_frame, image=scissor_img, command=lambda: play_game("scissor")).pack(padx=20)

# Clear button
reset_button = Button(window, text="RESET", font=("Times", 15, "bold"), width=10, command=reset_game)

window.mainloop()
