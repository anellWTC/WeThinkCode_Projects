
# TODO: Decompose into functions
def move_square(size):
    ''' movement of square '''
    
    print("Moving in a square of size "+str(size))
    for i in range(4):
        degrees = 90
        print("* Move Forward "+str(size))
        print("* Turn Right "+str(degrees)+" degrees")


def move_rectangle(length,width):
    ''' movement of rectangle '''
    print("Moving in a rectangle of "+str(length)+" by "+str(width))
    for i in range(2):
        degrees = 90
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")
        print("* Move Forward "+str(width))
        print("* Turn Right "+str(degrees)+" degrees")


def move_circle():    
    ''' movement of circle '''
    print("Moving in a circle")
    length = 1
    degrees = 1
    for i in range(360):
        print("* Move Forward "+str(length))
        print("* Turn Right "+str(degrees)+" degrees")


def square_dance(length):
    ''' moves in three squares '''
    print("Square dancing - 3 squares of size 20")
    for i in range(3):
        print("* Move Forward "+str(length))
        move_square(length)


def crop_circle(length):
    ''' crop circle '''
    print("Crop circles - 4 circles")
    for i in range(4):
        print("* Move Forward "+str(length))
        move_circle()


''' Give the robot directions/instructions and it performs the operation, which is the movement of the toy robot. Hence, i would give the name operation '''
def move():
    size = 10
    length = 20
    width = 10
    move_square(size)
    move_rectangle(length,width)
    move_circle()
    square_dance(length)
    crop_circle(length)


def robot_start():
    move()


if __name__ == "__main__":
    robot_start()
