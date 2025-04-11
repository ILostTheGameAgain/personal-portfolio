#Alec George Battle Simulator

#profile management, will save/load to csv file
import csv

#base stats for characters are random, needs import random
import random

#import small functions
from BS_small_functions import *


#function for assigning starting stats to a character
def assign_stats(level):
    #make a list of skill points, 1 is attack, 2 is defense, 3 is health, and 4 is speed
    skill_points= [1,2,3,4] #start with 1 of each
    for i in range(level):
        skill_points.append(random.randint(1,4))

    #count results by going through the list and increasing skill point counts based on how many times they're in the list
    strength = 0
    defense = 0
    health = 0
    speed = 0

    for point in skill_points:
        #if point is 1, increase strength by 2
        if point == 1:
            strength += 2

        #if point is 2, increase defense by 1
        elif point == 2:
            defense += 1

        #if point is 3, increase health by 5
        elif point == 3:
            health += 5

        #if point is 4, increase speed by 1
        elif point == 4:
            speed += 1

    #return stats
    return strength, defense, health, speed


#function to count the amount of skill points
def count_points(strength, defense, health, speed):
    str_count = strength//2
    def_count = defense
    hlt_count = health//5
    spd_count = speed

    total = str_count + def_count + hlt_count + spd_count - 4 #-4 to make up for starting amounts

    return total


#function to format profiles to display
def format_profiles(profiles):
    formatted_list = "\n"
    for i in range(len(profiles['name'])):
        formatted_list += f"{i+1}  Level {profiles['level'][i]} {profiles['name'][i]}\n"

    return formatted_list


#main function to manage profiles
def main():

    #put profiles in a list
    profiles = load_profiles()
    


    #function to add new profile
    def new_profile():
        #ask for information name and level, stats are assigned randomly based on level
#        name = is_unique(name_profiles(profiles), input("\nwhat is the name? "))
        name = input("\nwhat is the name? (leave blank to be random) ")
        if name == "":
            name = rand_name()
            print(f"\nname is {name}\n")

        level = is_int(input("\nwhat is the character's level? "))
        #randomly assign base stats
        strength, defense, health, speed = assign_stats(level)

        #add to the list of profiles
        profiles['name'][len(profiles['name'])] = name
        profiles['strength'][len(profiles['strength'])] = strength
        profiles['defense'][len(profiles['defense'])] = defense
        profiles['health'][len(profiles['health'])] = health
        profiles['speed'][len(profiles['speed'])] = speed
        profiles['level'][len(profiles['level'])] = level
        


    #function to edit a profile, increase skill points in specific categories if level is high enough
    def edit_profile(profile):
        #check if total skill points are less than the level
        if profiles["level"][profile] > count_points(profiles["strength"][profile], profiles["defense"][profile], profiles["health"][profile], profiles["speed"][profile]):
            #if yes, ask user what to do
            print("\nwhat would you like to do? Type:\n1 to add 1 strength point (2 strength)\n2 to add 1 defense point (1 defense)\n3 to add 1 health point (10 health)\n4 to add 1 speed point (1 speed)\n5 to go back\nYour answer here: ")
            action = is_int(input())

            #if action is 1, add 2 strength
            if action == 1:
                profiles["strength"][profile] += 2

            #if action is 2, add 1 defense
            elif action == 2:
                profiles["defense"][profile] += 1

            #if action is 3, add 5 health
            elif action == 3:
                profiles["health"][profile] += 5

            #if action is 4, add 1 speed
            elif action == 4:
                profiles["speed"][profile] += 1

            #if action is 5, change nothing
            elif action == 5:
                pass
            
            return f"\nsuccessfully updated profile\n"

        else:
            return "\nyou've spent all your skill points\n"
        

    #ask user for what they want to do repeatedly
    while True:
        print("\nwhat would you like to do? Type:\n1 to make a new profile\n2 to edit a profile\n3 to view profiles\n4 to view a specific profile's stats\n5 to view stats on all profiles\n6 to exit\nYour answer here:")
        user_input = is_int(input())

        #if user input is 1, create a new character
        if user_input == 1:
            cs()
            new_profile()

            #save changes
            save_profiles(profiles)

        #if user input is 2, edit a character
        elif user_input == 2:
            cs()
            #only do if the profile is actually in list
            editing_profile_name = input("\nwhat is the name of the profile you are editing?\n")
            if is_in_list(profiles["name"], editing_profile_name):
                #edit profile with index of the one that matches the name
                edited_profile_index = is_in_list(profiles["name"], editing_profile_name)-1
                print(edit_profile(edited_profile_index))

            #save changes
            save_profiles(profiles)

        #if user input is 3, display all profiles
        elif user_input == 3:
            cs()
            print(format_profiles(profiles))

        #if user input is 4, allow the user to see a graph of a specific profile's stats
        elif user_input == 4:
            profile_name = input("\nwhat is the name of the profile you are viewing? (type nothing to go back)\n")
            #check if the user input is blank to exit, and check to make sure the profile is in the list
            if profile_name == "":
                continue

            if is_in_list(profiles['name'], profile_name):
                pfp_index = is_in_list(profiles['name'], profile_name)
                #display the data for the profile
                print(f"""\n{profiles['name'][pfp_index-1]}'s stats:
Strength: {profiles['strength'][pfp_index-1]} ({profiles['strength'][pfp_index-1]//2-1} points)
Defense: {profiles['defense'][pfp_index-1]} ({profiles['defense'][pfp_index-1]-1} points)
Health: {profiles['health'][pfp_index-1]} ({profiles['health'][pfp_index-1]//5-1} points)
Speed: {profiles['speed'][pfp_index-1]} ({profiles['speed'][pfp_index-1]-1} points)
Level: {profiles['level'][pfp_index-1]}
""")
                graph([profiles['strength'][pfp_index-1]//2-1,profiles['defense'][pfp_index-1]-1,profiles['health'][pfp_index-1]//5-1,profiles['speed'][pfp_index-1]-1,profiles['level'][pfp_index-1]],['strength','defense','health','speed','level'])

            else:
                print("\nthat is not a profile")

        #graph average profile stats
        elif user_input == 5:
            cs()
            df = pd.DataFrame(profiles).describe()
            print(df)
            
            




        #if user input is 5, add to the csv and exit profile management
        elif user_input == 6:
            cs()
            #save list of profiles to csv
            save_profiles(profiles)

            break