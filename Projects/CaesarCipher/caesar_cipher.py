letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encryptor(message,number):
    message=list(message)
    for i in range(len(message)):
        for j in range (len(letters)):
            if message[i]==letters[j]:
                message[i]=letters[(number+j)%26]
                break
    return "".join(message)



def decryptor(message,number):
    message=list(message)
    for i in range(len(message)):
        for j in range (len(letters)):
            if message[i]==letters[j]:
                message[i]=letters[(number-j)%26]
                break
    return "".join(message)



print('''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88  ''')
while True:
    requirement=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message=input("Type your message\n")
    shift=int(input("Type the shift number:\n"))
    if(requirement.lower()=="encode"):
        print(f"Here is the encoded result: {encryptor(message,shift)}")
    elif(requirement.lower()=="decode"):
        print(f"Here is the decoded result: {decryptor(message,shift)}")
    stop=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if(stop.lower()=="no"):
        print("Goodbye")
        break
