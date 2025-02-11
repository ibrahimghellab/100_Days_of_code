from art import print_art
import random
import os


def calculate_score(player_score,bot_score):
    if(player_score==21):
        print("Win with a Blackjack 😎")
    elif(bot_score==21):
        print("Lose, opponent as Blackjack 🫠")
    elif(player_score>=22):
        print("You went over. You lose 😒")
    elif(bot_score>=22):
        print("Opponent went over. You win 😁")
    elif(player_score<22 and bot_score<22 and player_score>bot_score):
        print("You Win 🙌")
    elif(player_score<22 and bot_score<22 and player_score<bot_score):
        print("You lose 😭")
    elif(player_score<22 and bot_score<22 and player_score==bot_score):
        print("What a draw 💀")



def check_as(l):
    l_sum=sum(l)

    while(11 in l and l_sum>=22):
        l[l.index(11)]=1

    l_sum=sum(l)

    return l_sum
    


cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
while(True):
    if(input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")=="y"):
        os.system('cls')
        print_art()
        
        player=[cards[random.randint(0,12)],cards[random.randint(0,12)]]
        your_sum=check_as(player)
        
        bot=[cards[random.randint(0,12)],cards[random.randint(0,12)]]
        bot_sum=check_as(bot)
        
        print(f"Your cards : {player}, current score : {your_sum}")
        print(f"Computer's first card: {bot[0]}")
        if(your_sum==21):
            print("Win with a Blackjack 😎")
        elif(bot_sum==21):
            print("Lose, opponent as Blackjack 🫠")
        else:
            choice=input("Type 'y' to get another card, type 'n' to pass: ")
            while(choice.strip().lower()=='y' and your_sum <22 ):
                
                new_random=random.randint(0,12)
                player.append(cards[new_random])
                your_sum=check_as(player)
                
                if(your_sum<22):
                    print(f"Your cards : {player}, current score : {your_sum}")
                    print(f"Computer's first card: {bot[0]}")
                    choice=input("Type 'y' to get another card, type 'n' to pass: ")
                    
                    
            if(your_sum<22):
                while(bot_sum<17):
                    new_random=random.randint(0,12)
                    bot.append(cards[new_random])
                    bot_sum=check_as(bot)
            
            print(f"Your final hand: {player}, final score: {your_sum}")
            print(f"Computer's final hand: {bot}, final score: {bot_sum}")

            calculate_score(player_score=your_sum,bot_score=bot_sum)
           
    else:
        break
