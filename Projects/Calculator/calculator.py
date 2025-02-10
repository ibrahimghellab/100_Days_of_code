from art import print_art
import os

print_art()
first_number=float(input("What's the first number?: "))
while(True):
    
    print("""
+
-
*
/
          """)
    operation=input("Pick an operation: ")
    while(operation not in "+-/*"):
            operation=input("Pick an operation: ")
    second_number=float(input("What's the next number?: "))
    
    
    result=0
    if(operation=="+"):
        print(result:=first_number+second_number)
    elif(operation=="-"):
        print(result:=first_number-second_number)
    elif(operation=="*"):
        print(result:=first_number*second_number)
    elif(operation=="/"):
        print(result:=first_number/second_number)
        
    
    choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if(choice.strip().lower()=="y"):
        first_number=result
    else:
        os.system('cls')
        print_art()
        first_number=float(input("What's the first number?: "))