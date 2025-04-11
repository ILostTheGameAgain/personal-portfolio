#page for functions that could be used anywhere

#function to test if something is an integer
def is_int(value):
    try:
        int(value)
    except:
        value = is_int(input('\nThis only accepts integers, try again.\n'))
    return int(value)

#function to clear the screen
def cs():
    print('\033c')


#function to pause the screen until user input
def pause():
    input('\npress enter to continue.\n')