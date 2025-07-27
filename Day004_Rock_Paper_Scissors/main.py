from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

user_choice = int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors \n>>"))
npc_choice = randint(0,2)

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and npc_choice == 2:
    print("You win!")
elif user_choice == 2 and npc_choice == 0:
    print("You lose!")
elif npc_choice > user_choice:
    print("You lose")
elif user_choice > npc_choice:
    print("You win!")
elif npc_choice == user_choice:
    print("It´s a draw!")
    