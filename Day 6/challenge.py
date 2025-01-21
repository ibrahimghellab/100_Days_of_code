def jump():
    turn_left()
    move()
    for i in range(2):
        turn_left()
        turn_left()
        turn_left()
        move()
    
    turn_left()
for i in range(6): 
    move()
    jump()
    

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json