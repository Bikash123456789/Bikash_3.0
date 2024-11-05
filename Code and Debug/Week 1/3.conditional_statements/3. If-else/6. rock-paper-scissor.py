import random

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

user_choice = input("Enter your choice: ")
print(f"computer choice is {computer_choice}")


# My Code
# if computer_choice == user_choice:
#     print("Its a tie")
# else:
#     if computer_choice == "rock":
#         if user_choice == "paper":
#             print("user_wins")
#         else:
#             print("computer wins")
#     elif computer_choice == "paper":
#         if user_choice == "scissors":
#             print("User wins")
#         else:
#             print("Computer Wins")
#     else:
#         if user_choice == "rock":
#             print("user wins")
#         else:
#             print("Computer wins")

if computer_choice == user_choice:
    print("Its a tie")
elif (
    user_choice == "rock"
    and computer_choice == "paper"
    or user_choice == "paper"
    and computer_choice == "scissors"
    or user_choice == "scissors"
    and computer_choice == "rock"
):
    print("computer wins")
else:
    print("user wins")
