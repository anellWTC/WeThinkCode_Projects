def robot_start():
    """This is the entry function, do not change"""
    name = user_name()
    command_input(name)
    pass

'''
    Requires input from user to enter a name
'''
def user_name():
    name = input("What do you want to name your robot? ").upper()
    print(f"{name}: Hello kiddo!")
    return name 

'''
    Command function is taking the input from the user and determining if the input is invalid/valid.
    Checking if user is requesting forward,backward,left,right function
    This function is key to running the program and determining the function to be used
'''
def command_input(name):
    current_position = "front"
    x = 0
    y = 0
    # directions = "Starting point"
    command = ""
    while command != "off": 
        command = input(f"{name}: What must I do next? ")
        command = command.lower()
        if command == "off":
            print(f"{name}: Shutting down..")
        elif command == "help":
            help_command()
        elif "forward" in command.lower():
            x,y = move_forward(name, command,current_position,x,y)
            print(f" > {name} now at position ({x},{y}).")
        elif "sprint" in command.lower():
            x,y = sprint(name, command,current_position,x,y)
            print(f" > {name} now at position ({x},{y}).")
        elif "back" in command.lower():
            x,y = move_backward(name, command,current_position,x,y)
            print(f" > {name} now at position ({x},{y}).")
        elif command == "right":
            current_position = direction(command,current_position)
            move_right(name,x,y,command,current_position)
            # print(f" > {name} now at position ({x},{y}).")
        elif command == "left":
            current_position = direction(command,current_position)
            move_left(name,x,y,command,current_position)
            # print(f" > {name} now at position ({x},{y}).")
        else:
            print(f"{name}: Sorry, I did not understand '{command.capitalize()}'." )

'''
    When the user types in help it will display the information from the function below
    This function informs the user of the possible / valid input
'''
def help_command():
    print("""I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula""")

'''
    Checks if the length is 2 for e.g "forward 10" it has two characters entered it will split it and use the integer value,which will be [1] in the index
    It will then take the integer value and insert it in the co - ordinates depending on the positioning(x,y) 
    When back is typed in the command variable it will first check the current direction of the robot,
    from there it will move backward based on the value the user enters.
    The x and y co-ordinates will change regarding the current direction it is currently in.
'''
def move_forward(name, command,current_position,x,y):
    steps = command.split()
    if len(steps) != 2:
        print(f"{name}: Sorry, I did not understand '{command}'.")
    else:
        if current_position == "front":
            if y + int(steps[1]) > 200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:    
                steps[1] = int(steps[1])
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
                steps_y = steps[1]
                y += steps_y
        elif current_position == "right":
            if x + int(steps[1]) > 100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
            else:
                steps[1] = int(steps[1])
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
                steps_x = steps[1]
                x += steps_x
                
        elif current_position == "back":
            if y - int(steps[1]) < -200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                
            else:
                steps[1] = int(steps[1])
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
                steps_y = steps[1]
                y -= steps_y
                
        else:
            if x - int(steps[1]) < -100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                
            else:
                current_position == "left"
                steps[1] = int(steps[1])
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
                steps_x = steps[1]
                x -= steps_x
                

    return x , y
'''
    Checks if the length is 2 for e.g "forward 10" it has two characters entered it will split it and use the integer value,which will be [1] in the index
    It will then take the integer value and insert it in the co - ordinates depending on the positioning(x,y) 
    When back is typed in the command variable it will first check the current direction of the robot,
    from there it will move backward based on the value the user enters.
    The x and y co-ordinates will change regarding the current direction it is currently in.
'''
def move_backward(name, command,current_position,x,y):
    steps = command.split()
    if len(steps) != 2:
        print(f"{name}: Sorry, I did not understand '{command}'.")
    else:
        if current_position == "front":
            if y - int(steps[1]) < -200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                
            else: 
                steps[1] = int(steps[1])
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
                steps_y = steps[1]
                y -= steps_y
            
        elif current_position == "right":
            if x - int(steps[1]) < -100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                
            else:
                steps[1] = int(steps[1])
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
                steps_x = steps[1]
                x -= steps_x
                
        elif current_position == "back":
            if y + int(steps[1]) > 200:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                
            else:
                steps[1] = int(steps[1])
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
                steps_y = steps[1]
                y += steps_y
                
        else:
            if x + int(steps[1]) > 100:
                print(f"{name}: Sorry, I cannot go outside my safe zone.")
                
            else:
                current_position == "left"
                steps[1] = int(steps[1])
                print(f" > {name} moved {steps[0]} by {steps[1]} steps.")
                steps_x = steps[1]
                x += steps_x
                
    return x , y

''' 
    When right is typed the following will appear.
    and give the co ordinates of where the robot currently is.
    When position is in right it determines the x coordinate 
'''
def move_right(name,x,y,command,current_position):
    if command == "right":
        print(f" > {name} turned right.")
        print(f" > {name} now at position ({x},{y}).")
    return x, y

''' 
    When left is typed the following will appear.
    and give the co ordinates of where the robot currently is
    When position is in left it determines the x coordinate  
'''
def move_left(name,x,y,command,current_position):
    if command == "left":
        print(f" > {name} turned left.")
        print(f" > {name} now at position ({x},{y}).")
    return x, y



''' Function determining/locating the current position of the robot ''' 
def direction(command,current_position):
    if command == "right" and current_position == "front"  :
        current_position = "right"
    elif command == "right" and current_position == "right"  :
        current_position = "back"
    elif command == "right" and current_position == "back"  :
        current_position = "left"
    elif command == "right" and current_position == "left"  :
        current_position = "front"
    elif command == "left" and current_position == "front"  :
        current_position = "left"
    elif command == "left" and current_position == "left"  :
        current_position = "back"
    elif command == "left" and current_position == "back"  :
        current_position = "right"
    elif command == "left" and current_position == "right"  :
        current_position = "front"
        
    return current_position

'''
    Function makes the toy robot sprint, meaning it will move forward faster/quicker
    Recursion being used 
'''
def sprint(name, command,current_position,x,y):
    steps = command.split()
    if len(steps) != 2:
        print(f"{name}: Sorry, I did not understand '{command}'")
    else:
        if steps[1] != "0":
            x,y = move_forward(name,"forward "+ str(steps[1]),current_position,x,y)
            command = "sprint " + str(steps[1])
            x,y = sprint(name,steps[0] +" "+ str(int(steps[1]) -1),current_position,x,y)
    return x,y 

if __name__ == "__main__":
    robot_start()