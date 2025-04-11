#Alec George coin change problem

#to read csv, import pandas
import pandas as pd


#functoin to see if something is in a list
def is_in_list(value, items1, items2):
    value = value.strip().lower()
    if value in items1:
        return value
    
    elif value in items2:
        return value
    else:
        print(f"\nthat is not an optoin. Your optoins are:\ndollars (us)\npounds (uk)\neuros(no specific place)\nkronor (sweden)\n")
        value = is_in_list(input('what coin type are you using?\n'), items1,items2)

    return value


#functoin to check if something is an integer
def is_float(value):
    try:
        float(value)
    except:
        value = is_float(input('\nthat is not a number. Try again\n'))

    return float(value)


#functoin to check if something is greater than 0
def is_positive(value):
    if value <= 0:
        value = is_positive(is_float(input('\nNumber must be greater than 0. Try again\n')))
        
    return value


#main functoin to run everything else
def main():
    #variable for the available coins
    coins = {
        'name': [],
        'value': []
    }


    #make coins into a dataframe
    df = pd.read_csv('CC_values.csv')
    #make it a dictionary
    df = df.to_dict()

    #functoin to add the right coin types to the list
    def add_coins(ct):
        for index, typ in enumerate(df['type'].values()):
            if typ == ct:
                coins['name'].append(df['name'][index])
                coins['value'].append(df['value'][index])

        for index, typ in enumerate(df['country'].values()):
            if typ == ct:
                coins['name'].append(df['name'][index])
                coins['value'].append(df['value'][index])


    #functoin to calculate the right coins to add to get target amount
    def caclate(amt):
        coin_string = 'needed coins/bills/notes:'
        #do for every coin
        for i in range(len(coins['name'])):
            repeats = 0
            #subtract the coin that can still fit in the amont repeatedly
            while amt > 0:
                amt -= coins['value'][-(i+1)]
                repeats += 1

            if amt < 0:
                amt += coins['value'][-(i+1)]
                repeats -= 1

            #add to string if there are more than one
            if repeats > 0:
                coin_string += f'\n{repeats} {coins['name'][-(i+1)]}'

        return coin_string

    #repeat until the user wants to stop
    while True:

        #variable for the available coins
        coins = {
            'name': [],
            'value': []
        }

        
        #tell user instructoins
        print("""
    Welcome to the coin change problem!
    To use, input the coin type you are using
    Then, input the total amount of money you want
    This will then tell you the minimum number of coins, bills, and notes to have that amount of money.
    """)
        
        #ask user for coin type
        coin_type = is_in_list(input("\nwhat is the name of the coin type/country?\n"), df['type'].values(), df['country'].values())
        add_coins(coin_type)

        #ask user for amount
        amount = is_positive(is_float(input(f"\nWhat is the amount?\n")))

        #print the number of coins
        print(caclate(amount))

        if input('\nto generate again, type anything and push enter\nto quit, type nothing and push enter\n'):
            pass
        else:
            break
