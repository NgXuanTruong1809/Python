def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
display(row1,row2,row3) 

def user_choice():
    #variables 

    #initial
    choice = 'Wrong'
    acceptable_range = range(0,3)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input("Enter a number (0-2): ")
        if choice.isdigit() == False:
            print("That is not a digit !")
        else :
            if int(choice) not in acceptable_range:
                print("Your choice not in 0 -> 2 ")
            else :
                within_range = True
    return int(choice) 

###BAI TAP NHO

def display_list(mylist):
    print(f'Here is your list: {mylist}')

def replacement_choice(mylist, position):
    user_placcement  = input("Type a string to place at position: ")
    mylist[position] = user_placcement
    return mylist

def gameon_choice():
    choice = 'Wrong'
    while choice.upper() not in ['Y','N']:
        choice = input("Keep playing ? (Y or N) ")
        if choice.upper() not in ['Y','N']:
            print("Sorry, invalid choice !")

    if choice.upper() == 'Y':
        return True
    else:
        return False

game_on = True 
game_list = ['1','2','3']

while game_on:
    display_list(game_list)
    position_replace = user_choice()
    game_list = replacement_choice(game_list, position_replace)
    display_list(game_list)
    game_on = gameon_choice()
    


        

