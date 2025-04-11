#Alec George Battle Simulator

#page with some small quality of life functions

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from faker import Faker

#function to clear screen
def cs():
    print("\033c")


#function for exception handling (integers)
def is_int(value):
    try:
        int(value)

    except:
        value = is_int(input("\nPlease input an integer.\n"))
    return int(value)


#function to check if a number is in a range
def is_in_range(value, min, max):
    value = is_int(value)

    if value < min or value > max:
        value = is_in_range("\ninvalid input, try again.\n", min, max)
    return value


#function to check if something is unique in a list
def is_unique(list, value):

    #check every value in the list
    for item in list:
        if item == value:
            value = is_unique(list, input("\nThat item already exists. Choose something else.\n"))
            
    return value



#function to check if something is in a list
def is_in_list(list, value):
    for index in range(len(list)):
        if list[index] == value:
            return index+1 #add one so it isn't considered false
        
    return False


#function to put all profiles in a list
def load_profiles():
    #list of profiles, comes from folder
    profiles = pd.read_csv('battle_simulator/BS_character_info.csv')
    return profiles.to_dict()


#function to put profiles list into csv
def save_profiles(profiles):
    profiles = pd.DataFrame(profiles)
    profiles.to_csv('battle_simulator/BS_character_info.csv', index=False)


#function to display a bar graph of values
def graph(values, titles):
    plt.bar(titles, values)

    plt.show()

#function to generate a random name
def rand_name():
    fake = Faker()

    return fake.name()