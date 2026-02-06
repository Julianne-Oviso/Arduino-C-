def main():
    x = None
    y = None
    while x is None or y is None:
        try:
            user_input_x = input("Enter the x value: ")
            user_input_y = input("Enter the y value: ")
            x = float(user_input_x)
            y = float(user_input_y)
            print("x =", x, "y =", y)
        except ValueError:
            print("Error: Invalid input. Please make sure both x and y values are numbers.")
            x = None
            y = None
    print("Done with challenge")

main()
