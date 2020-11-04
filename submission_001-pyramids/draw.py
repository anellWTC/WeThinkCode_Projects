

# TODO: Step 1 - get shape (it can't be blank and must be a valid shape!)
def get_shape():
    shape = input("Shape?: ").lower()
    while (shape != "pyramid" and shape != "square" and shape != "triangle" and shape != "upside down triangle" and shape != "cone" and shape !="rectangle"):
        shape = input("Shape?: ").lower()
    return shape


# TODO: Step 1 - get height (it must be int!)
def get_height():
    height = (input("Height?: "))
    while height.isdigit() == False:
        height = (input("Height?: "))
    height = int(height)
    while height > 80 or height < 1:
        height = int(input("Height?: "))
    return height

# TODO: Step 2
def draw_pyramid(height, outline):  
    if outline == False:
        for i in range(height):
            for j in range(1,height - i):
                print(" " , end="")
            for j in range(0,i*2+1):
                print("*", end = "")
            print("")
    if outline == True:
        for i in range(height):
            for j in range(height-(i+1)):
                print(" ", end="")
            for j in range(2*i+1):
                if j==0 or j==2*i or i==height-1:
                    print("*",end="")
                else:
                    print(" ", end="")
            print()

# TODO: Step 3
def draw_square(height, outline):
    if outline == False:
        for i in range(height):
            for j in range(height):
                print("*", end = "")
            print()
    if outline == True:
        for i in range(1, height + 1):
            for j in range (1, height + 1):
                if i == 1 or i == height or j == 1 or j == height * 1:
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print()


# TODO: Step 4
def draw_triangle(height, outline):
    if outline == False:
        for i in range(0,height):
            for j in range(0, i+1):
                print("*" , end="")
            print()
    if outline == True:
        for i in range(height):
            for j in range(height-i):
                print("", end="")
            for j in range(1*i+1):
                if j==0 or j==1*i or i==height-1:
                    print("*",end="")
                else:
                    print(" ", end="")
            print()

def draw_upside_down_triangle(height, outline):
    if outline == False:
        for i in range(height):
                    for j in range(height - i):
                        print("*", end = "")
                    print()
    if outline == True:
        for i in range(height -1, -1, -1):
            for j in range(height):
                print("", end = "")
            for j in range(i+1):
                if j == 0 or j == i or i == height-1:
                    print("*", end = "")
                else:
                    print(" ", end = "")
            print()

def draw_cone(height, outline):
    if outline == False:
        for i in range(height-1,-1,-1):
            for j in range(0,height - i):
                print(" " , end="")
            for  k in range(0,i*2+1):
                print("*", end = "")
            print("")
    if outline == True:
        for i in range(height-1,-1,-1):
            for j in range(height-i):
                print(" ", end="")
            for j in range(2*i+1):
                if j==0 or j==2*i or i==height-1:
                    print("*",end="")
                else:
                    print(" ", end="")
            print()

def draw_rectangle(height, outline):
    if outline == False:
        for i in range(height):
            for j in range(height*3):
                print("*", end = "")
            print()
    if outline == True:
        for i in range(1, height + 1):
            for j in range (1, height*3 + 1):
                if (i == 1 or i == height or j == 1 or j == height * 3):
                    print("*", end = "")
                else:
                    print("", end = " ")
            print()



# TODO: Steps 2 to 4, 6 - add support for other shapes
def draw(shape, height, outline):
    if shape == "pyramid":
        draw_pyramid(height,outline)
    if shape == "square":
        draw_square(height,outline)
    if shape == "triangle":
        draw_triangle(height,outline)
    if shape == "upside down triangle":
        draw_upside_down_triangle(height,outline)
    if shape == "cone":
        draw_cone(height,outline)
    if shape == "rectangle":
        draw_rectangle(height,outline)

# TODO: Step 5 - get input from user to draw outline or solid
def get_outline():
    outline = False
    draw = input("Outline only? (y/N):")
    while (draw != "y" and draw != "N"):
        print("\nAnswer with y/N\n")
        draw = input("Outline only? (y/N):")
    if draw == "y":
        outline = True
    if draw == "N":
        outline = False
    return outline


if __name__ == "__main__":
    shape_param = get_shape()
    height_param = get_height()
    outline_param = get_outline()
    draw(shape_param, height_param, outline_param)

