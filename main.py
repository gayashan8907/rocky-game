from drawings import rock,paper,scissors
import random

art_works = [rock,paper,scissors]

def winner(user, computer):
    if user == computer:
        return f"Game draw"
    elif user == 1 and computer == 3 or user == 3 and computer == 2 or user == 2 and computer == 1:
        return f"You win"
    else:
        return f"Computer win"

continue_game = True

while continue_game:
    user_choice = int(input('Enter 1 for Rock,2 for Paper and  3 for Scissor : '))
    if user_choice >3 or user_choice<1:
        raise ValueError("The number must be 1,2,or 3")
    computer_choice = random.randint(1,3)
    print(f"Your choice\n{art_works[user_choice-1]} ")

    print(f"computer choice\n {art_works[computer_choice-1]}")

    print(winner(user_choice,computer_choice))
    end_game = input("If you want to continue type continue or  want to exit type exit:").lower()
    if end_game=='exit':
        continue_game=False