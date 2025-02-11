from art import print_art
import random
import os


cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

if(input("Do you want to play a game of BlackJack? Type 'y' or 'n':")=="y"):
    print_art()
    your_sum=0
    bot_sum=0
    player=[cards[random.randint(0,12)],cards[random.randint(0,12)]]
    your_sum+=sum(player)
    bot=[cards[random.randint(0,12)],cards[random.randint(0,12)]]
    bot_sum+=sum(bot)
    
    print(f"Your cards : {player}, current score : {your_sum}")
    print(f"Computer's first card: {bot_sum}")
    if(your_sum==21):
        print("something")
    elif(bot_sum==21):
        print("something else")
    else:
        choice=input("Type 'y' to get another card, type 'n' to pass: ")
        while(choice.strip().lower()=='y' and your_sum <22 ):
            
            new_random=random.randint(0,12)
            player.append(cards[new_random])
            your_sum+=cards[new_random]
            print(f"Your cards : {player}, current score : {your_sum}")
            print(f"Computer's first card: {bot_sum}")
            if(your_sum<22):
                choice=input("Type 'y' to get another card, type 'n' to pass: ")

        while(bot_sum<17):
            new_random=random.randint(0,12)
            bot.append(cards[new_random])
            bot_sum+=cards[new_random]
        
        print(f"Your final hand: {player}, final score: {your_sum}")
        print(f"Computer's final hand: {bot}, final score: {bot_sum}")


        if(your_sum==21):
            print("Win with a Blackjack 😎")
        elif(bot_sum==21):
            print("Loose with an opposent Blackjack 🫠")
        elif(your_sum>=22):
            print("You went over. You lose 😒")
        elif(bot_sum>=22):
            print("Opponent went over. You win 😁")
        elif(your_sum<22 and bot_sum<22 and your_sum>bot_sum):
            print("You Win 🙌")
        elif(your_sum<22 and bot_sum<22 and your_sum<bot_sum):
            print("You loose 😭")



#ordonne le code met les conditions au bon moment avec des if else 