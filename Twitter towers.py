import math

# This function takes dimensions of a rectangle by input from the user,
# if the rectangle is a square or the difference between the lengths of its sides is greater than 5, 
# the area of the rectangle will be printed
# else, its scope will be printed
def creation_rectangle():
    height = int(input("Please enter the height of the tower: ")) # Correct input is guaranteed
    width = int(input("Please enter the width of the tower: ")) # Correct input is guaranteed
    if height == width or height > 5 + width or height + 5 < width:
        print("\nThe area of the rectangle is:", height * width)
    else:
        print("\nThe scope of the rectangle is:", 2 * (height + width))

#This function gets the length and width of a triangle and draws it on the screen
def draw_triangular(height, width):
    if width % 2 == 0 or width > 2 * height:
        print("Cannot print this triangular tower triangular")
        return
    print("A triangular tower in width:", width, "and height:",height, "will look like this:\n")
    for i in range(width // 2):
        print(" ", end="")
    print("*")
    mid_lines = (width - 3) // 2
    if(height==2):
        times=0
    else:
        times = (height - 2) // mid_lines
    
    rest = height - 2 - mid_lines * times
    for j in range(rest):
        for i in range(width // 2 - 1):
            print(" ", end="")
        print("***")
    for i in range(1, width // 2):
        for j in range(times):
            for k in range(width // 2 - i):
                print(" ", end="")
            for k in range(i):
                print("**", end="")
            print("*")
    for i in range(width):
        print("*", end="")
    print("\n")

# This function takes dimensions of a triangle by input from the user,
# then asking for input from the user, if the user selects '1', they will be shown the perimeter of the triangle.
# if  the user selects '2' the draw_triangular function will be called which will draw the triangle on the screen.
def creation_triangular():
    height = int(input("Please enter the height of the tower: "))
    width = int(input("Please enter the width of the tower: "))
    print("What do you want to check?")
    print("1. Check the perimeter of the triangle")
    print("2. See what the tower looks like")
    option = input()
    while option not in ['1', '2']:
        print("Invalid input, please try again")
        option = input()
    if option == '1':
        print("The perimeter of the triangle is:", width + 2 * math.sqrt((width / 2) ** 2 + height ** 2))
    elif option == '2':
        draw_triangular(height, width)

# This main function presents a main menu to the user and calls the appropriate function for the request.
def main():
    option = 0
    print("Welcome to our program,")
    print("We will help you research different types of towers in the most convenient way.")
    while option != 3:
        print("\nMain menu\nPlease select the tower you would like to build:")
        print("1. Rectangle tower")
        print("2. Triangular tower")
        print("3. End the program")
        choice = input() 
        try:           
            option = int(choice)
        except ValueError:
            print("")
        if option == 1:
            creation_rectangle()
        elif option == 2:
            creation_triangular()
        elif option == 3:
            print("We were happy to be of assistance to you")
        else:
            print("Invalid input, please try again")


if __name__ == "__main__":
    main()
