rock = '''rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''' 
import random

choices = [rock, paper, scissors]
choicenumber = random.randint(0,2)
computerchoice = choices[choicenumber]

selection = int(input('Pick 0 for rock, 1 for paper, or 2 for scissors: '))
if selection == 0:
    print(rock)
elif selection == 1:
    print(paper)
elif selection == 2:
    print(scissors)
else:
    print("Try again")

if selection == choicenumber:
    # print(selection)
    print(computerchoice)
    print("It's a draw!")
elif selection == 0 and choicenumber == 1:
    # print(selection)
    print(computerchoice)
    print("Paper beats rock! You lose :-(")
elif selection == 0 and choicenumber == 2:
    # print(selection)
    print(computerchoice)
    print("Rock beats scissors! You win :-)")
elif selection == 1 and choicenumber == 0:
    # print(selection)
    print(computerchoice)
    print("Paper beats rock! You win :-)")
elif selection == 1 and choicenumber == 2:
    # print(selection)
    print(computerchoice)
    print("Scissors beats paper! You lose :-(")
elif selection == 2 and choicenumber == 0:
    # print(selection)
    print(computerchoice)
    print("Rock beats scissors! You lose :-(")
elif selection == 2 and choicenumber == 1:
    # print(selection)
    print(computerchoice)
    print("Scissors beats paper! You win :-)")
else:
    print("Something went wrong :-(")
