# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Maze
# Also did hurdle 1,2,3,4
def turn_around():
    for i in range (1,3):
        turn_left()

def turn_right():
    for i in range (1,4):
        turn_left()
        
def jump():
        turn_left()
        while not right_is_clear():
            move()
        turn_right()
        move()
        turn_right()
        while not right_is_clear():
            move()
        turn_left()
 


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
   
while front_is_clear():
    move
turn_left()
