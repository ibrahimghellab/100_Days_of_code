def calculate_love_score(first_name,second_name):
    first_number=0
    second_number=0
    for letter in first_name.lower():
        if letter in "true":
            first_number+=1
        if letter in "love":
            second_number+=1
    for letter in second_name.lower():
        if letter in "true":
            first_number+=1
        if letter in "love":
            second_number+=1
    
    print(f"{first_number}{second_number}")

    