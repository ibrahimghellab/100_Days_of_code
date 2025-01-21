import requests
response=requests.get("https://random-word-api.herokuapp.com/word")
user_find=[]
stages = [
'''    
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]
life=6
if response.status_code==200:
    word=response.json()[0]

print('''
 _                                           
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/''')

for i in range(len(word)):
    user_find.append("_")

while(word!=user_find and life>=0):
    print(f"Word to guess: {''.join(user_find)}")
    guess=input("Guess a letter: ").lower()
    find_letter=False
    for i in range(len(word)):
        if(word[i]==guess):
            user_find[i]=guess
            find_letter=True
    if(not find_letter):
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        life-=1
    print(stages[life])
    if(life==0):
        print(f"****************************IT WAS {word}! YOU LOOSE****************************")
        break
    else:
        print(f"****************************{life}/6 LIVES LEFT****************************")
 
    
