#Alec George Battle simulator

#will allow users to save info and battle each other
#profiles will have stats including level, xp, attack, defense, etc.
#user can create new character or battle other characters

#import functions from other pages to run on main
from BS_small_functions import *
from BS_guide import main as guide
from BS_profile_management import main as manage_profiles
from BS_battling import main as battle


#main function, runs other functions
def main():
    while True:
        #ask user what to do
        choice = is_int(input("""
Welcome to battle simulator!
What would you like to do? Type:
1 to battle someone else
2 to manage/create/view profiles
3 to learn what you're doing
4 to exit
Your answer here: """))
        #do things depending on what the user chose
        if choice == 1:
            battle()

        elif choice == 2:
            manage_profiles()

        elif choice == 3:
            guide()

        elif choice == 4:
            break