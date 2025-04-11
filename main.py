#Alec George Personal Portfolio

#will have 6 of the programs I made, allowing the user to try them out and see the things I make
#will include detailed instructions for each project


#import functions from other files
from extra_functions import *
from password_generator import generate_passwords
from BS_main import main as battle_simulator
from morse_code import main as morse_code
from coin_changer import main as coin_change


#main function, give instructions and ask user for input
def main():
    while True:
        cs()
        #variable for user input
        user_input = is_int(input('''PERSONAL PORTFOLIO
Below are a few projects that I've made in the past.
They are here for you to try.
Upon choosing to do one, you'll get more information about it.
What would you like to see? Type:
1 to view my password generator
2 to view my battle simulator
3 to view my morse code translator
4 to view my coin changer
7 to exit
Your answer here:
'''))
        if user_input == 1:
            cs()
            print('''PASSWORD GENERATOR
This program was a solo project for computer programming 2.
It allows you to generate random passwords.
It will allow you to specify requirements, including:
 + length
 + amount of letters (uppercase and lowercase)
 + amount of numbers
 + amount of special characters
 + number of passwords''')
            pause()
            generate_passwords()

            pause()

        elif user_input == 2:
            cs()
            print('''BATTLE SIMULATOR
This program was a solo project for computer programming 2.
It allows you to create profiles and:
 + level them up
 + fight other profiles
 + view stats
 + choose to upgrade stats
This project was used to teach about use of
multiple files and libraries.''')
            pause()
            battle_simulator()

            pause()

        elif user_input == 3:
            cs()
            print('''MORSE CODE TRANSLATOR
This program was a solo project for computer programming 2.
It allows you to
 + translate English to morse code
 + translate morse code to English''')
            pause()
            morse_code()

            pause()

        elif user_input == 4:
            cs()
            print('''COIN CHANGER
This program was a solo project for computer programming 2.
It allows you to:
 + give an amount of money in a type of currency
 + return the least number of coins/bills/notes 
   using that currency to reach the amount''')
            pause()
            coin_change()

            pause()

        elif user_input == 5:
            cs()
            print('''BATTLE SIMULATOR
This program was a solo project for computer programming 2.
It allows you to create profiles and:
 + level them up
 + fight other profiles
 + view stats
 + choose to upgrade stats
This project was used to teach about use of
multiple files and libraries.''')
            pause()
            battle_simulator()

            pause()

        elif user_input == 6:
            cs()
            print('''BATTLE SIMULATOR
This program was a solo project for computer programming 2.
It allows you to create profiles and:
 + level them up
 + fight other profiles
 + view stats
 + choose to upgrade stats
This project was used to teach about use of
multiple files and libraries.''')
            pause()
            battle_simulator()

            pause()

        
        elif user_input == 7:
            cs()
            print('thank you for viewing this portfolio.')
            break

        else:
            cs()
            print('That is not a valid input.\n')


main()
