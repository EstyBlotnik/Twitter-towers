import math


def creation_rectangle():
    height = int(input("Please enter the height of the tower: "))
    width = int(input("Please enter the width of the tower: "))
    if height == width or int(height) == 5 + int(width) or int(height) + 5 == int(width):
        print("The area of the rectangle is:", int(height) * int(width))
    else:
        print("The perimeter of the rectangle is:", 2 * (height + width))

    if height == width or height == 5 + width or height + 5 == width:
        print("The area of the rectangle is:", height * width)
    else:
        print("The perimeter of the rectangle is:", 2 * height + width)


def draw_triangular(height, width):
    if width % 2 == 0 or width > 2 * height:
        print("Cannot print the triangular")
        return
    for i in range(width // 2):
        print(" ", end="")
    print("*")
    mid_lines = (width - 3) // 2
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


def main():
    option = 0
    while option != 3:
        print("Main menu\nPlease select the tower you would like to build:")
        print("1. Rectangle tower")
        print("2. Triangular tower")
        print("3. End the program")
        choice = input()
        option = int(choice)
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
