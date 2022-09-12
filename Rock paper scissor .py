rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game = [rock, paper, scissors]

user_inp = int(input("select 0 for rock , 1 for paper , 2 for scissors."))
print(f" User chose {game[user_inp]}")

a = random.randint(0,2)
random_inp = game[a]
print(f" Opponent chose {random_inp}")

if user_inp > 2 or user_inp < 0 :
  print("invalid input from user")
elif user_inp == a :
  print("Draw")
elif user_inp == 0 and a == 1:
  print("Random user wins")
elif user_inp == 1 and a == 2:
  print("Random user wins")
elif user_inp == 2 and a == 0:
  print("Random user wins")
else:
  print("You win")