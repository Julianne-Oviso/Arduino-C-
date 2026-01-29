def main():
    print("Starting the code challenge") 
    user_input_good = False 
    while(user_input_good == False):
        my_num = input('enter a number > ') 
        try:
            my_num = int(my_num)
            user_input_good = True 
        except:
            print('Please enter a number') 
            print(my_num, 'is not a number') 
            # user_input_good = False 
    print(my_num, 'is a number')
    print('Done')
    
    print("Ending the code challenge")
main()
