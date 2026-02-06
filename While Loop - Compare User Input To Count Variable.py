def get_validated_input():
    while True:
        try:
            user_input = int(input("Please enter an integer number from 0 to 9: "))
            if 0 <= user_input <= 9:
                return user_input
            else:
                print("Input is outside the valid range. Please enter a number between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

user_variable = get_validated_input()

print(f"\nUser input: {user_variable}\n")

count_variable = 0
while count_variable <= 10:
    if user_variable == count_variable:
        print(f"The User variable is equal to the count variable. User = {user_variable} Count variable = {count_variable}")
    
    count_variable += 1 
