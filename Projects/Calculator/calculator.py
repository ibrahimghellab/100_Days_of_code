from art import print_art

print_art()
while(True):
    first_number=float(input("What's the first number?: "))
    print("""
    +
    -
    *
    /
          """)
    operation=input("Pick an operation: ")
    second_number=float(input("What's the next number?: "))
    
    if(operation=="+"):
        print(first_number+second_number)
    elif(operation=="-"):
        print(first_number-second_number)
    elif(operation=="*"):
        print(first_number*second_number)
    elif(operation=="/"):
        print(first_number/second_number)
    else:
        while(operation not in "+-/*"):
            operation=input("Pick an operation: ")
    
    choice=input(f"Type 'y' to contionue calculating with {}, or type 'n' to start a new calculation: ")