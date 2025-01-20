import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
result=[]
final_string=""
letters_choice=int(input("How many letters would you like in your password?\n"))
symbols_choice=int(input("How many symbols would you like in your password?\n"))
numbers_choice=int(input("How many numbers would you like in your password?\n"))

for i in range(letters_choice):
    result.append(random.choice(letters))
for i in range(symbols_choice):
    result.append(random.choice(symbols))
for i in range(numbers_choice):
    result.append(random.choice(numbers))
random.shuffle(result)
for i in range(len(result)):
    final_string+=result[i]
print(f"Your password is: {final_string}")