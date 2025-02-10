import os


stop=False
user_bid={}
while(not stop):

    print("""

                            ___________
                                    /
                            )_______(
                            |\"\"\"\"\"\"\"|_.-._,.---------.,_.-._
                            |       | | |               | | ''-.
                            |       |_| |_             _| |_..-'
                            |_______| '-'''---------'' '-'
                            )\"\"\"\"\"\"\"(
                            /_________\\
                        .-------------.
                        /_______________\\
    """)
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: $"))
    user_bid[name]=bid
    next=input("Are there any other bidders? Type 'y' for Yes, any other key otherwise: ").strip().lower()
    

    if(next!="y"):
        stop=True
    os.system('cls')
max_value=0
max_key=""
for key,value in user_bid.items():
    if(value>max_value):
        max_value=value
        max_key=key

print(f"The winner is {max_key} with a bid of ${max_value}")
    
    