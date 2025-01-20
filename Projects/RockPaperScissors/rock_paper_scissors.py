import random

rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

possibilities=[rock,paper,scissors]


rand=random.randint(0,2)

choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(possibilities[choice]+"\n")

print("Computer choose:")
print(possibilities[rand])

if(possibilities[choice]==possibilities[rand]):
    print("It's a draw")
elif((possibilities[choice]==rock and possibilities[rand]==paper) or (possibilities[choice]==paper and possibilities[rand]==scissors) or (possibilities[choice]==scissors and possibilities[rand]==rock)):
    print("You lose")
elif((possibilities[rand]==rock and possibilities[choice]==paper) or (possibilities[rand]==paper and possibilities[choice]==scissors) or (possibilities[rand]==scissors and possibilities[choice]==rock)):
    print("You win!")