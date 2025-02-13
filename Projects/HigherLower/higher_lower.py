import art
import json
import os
import random 
art.print_intro()
art.print_vs()

def generate_person(persons):
    index=random.randint(0,len(persons)-1)
    return persons[index]



def main():
    with open('data.json') as file:
        persons=json.load(file)

    a=generate_person(persons)
    b=generate_person(persons)
    cpt=0
    art.print_intro()
    while(True):
        if(len(persons)>1): 
            while(a==b):
                b=generate_person(persons)
            print(f"You're right! Current score: {cpt}")
            art.print_intro()
            print(f"Compare A : {a["name"]}, {a["description"]}, from {a["country"]}")
            art.print_vs()
            print(f"Against B : {b["name"]}, {b["description"]}, from {b["country"]}")
            choice=input("Who has more followers? Type 'A' or 'B': ")
            while(choice!='A' and choice!='B'):
                choice=input("Who has more followers? Type 'A' or 'B': ")
            os.system('cls')
            if(choice=='A' and a["follower_count"]>b["follower_count"]) or (choice=='B' and b["follower_count"]>a["follower_count"]):
                persons.remove(a)
                a=b
                cpt+=1
                
            else:
                art.print_intro()
                print(f"Sorry, that's wrong. Final score : {cpt}")
                break
        else:
            print(f"Congratulations! You have completed the game with a score of {cpt}! 🎉")
            break
              


if __name__=="__main__":
      main()