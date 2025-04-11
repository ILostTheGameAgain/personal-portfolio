#alec george financial calculator

#will do certain financial functions, uses math library
import math

#function to calculate how long it will take to save for a goal based on a weekly or montlhly deposit
def goal_save(price, monthly_amount):
    months = 0
    while price > 0:
        price -= monthly_amount
        months += 1
    return months


#function to calculate compound interest, will return the amount of money you'll have after a certain amount of time of compound interest, will recieve variables for starting amount, the growth %, the amount of time, and how often it grows
def compound_interest(start, percent, compound_rate, time):
    if compound_rate == 0:
        sum = round(round(start, 2)*math.e**((percent/100)*time), 2)
    else:
        sum = round(round(start, 2)*(1+((percent/100)/compound_rate))**(compound_rate*time), 2)
    return f"{sum :.2f}"


#function to calculate budget, will make a list of things to add to the budget, and divide the total amount among them
def budget(items, total):
    return_string = ""
    for i in range(len(items[0])):
        return_string += f"{items[0][i]}: ${items[1][i]*100/total:.2f}\n"

    return return_string


#function to make a list of items for the budget, along with their amount
def list_items():
    total_percent = 0
    item_list = []
    percent_list = []
    while True: #stupid proof
        while total_percent < 100:
            item_list.append(input(" item: "))
            percent_list.append(int(input(" percent of budget: ")))
            total_percent += percent_list[-1]
            print(f" {100-total_percent}% of your budget is left\n")

        if total_percent > 100:
            total_percent -= percent_list[-1]
            percent_list[-1] = 100-total_percent
            return [item_list, percent_list]
            
            
        else:
            return [item_list, percent_list]


#function to calculate discounts to prices
def discount(price, discount):
    new_price = price - round((discount/100)*price, 2)
    return f"{new_price :.2f}"


#function to calculate tips
def tip(price, tip, people):
    tip_price = round(((tip/100)*price)/people, 2)
    return f"{tip_price:.2f}"


#main function
def main(user_choice):
    if user_choice == 1:
        return f"it would take {round(goal_save(round(float(input(" goal: ")), 2), round(float(input(" monthly deposit amount: ")), 2)))} months"
    elif user_choice == 2:
        return f"${compound_interest(round(float(input(" start amount: ")), 2),float(input(" annual interest amount: ")),float(input(" compound rate (yearly is 1, monthly is 12, daily is 365, continuous is 0): ")), float(input(" time (years): ")))}"
    elif user_choice == 3:
        return budget(list_items(), round(float(input(" amount of money: ")), 2))
    elif user_choice == 4:
        return discount(round(float(input(" original price: ")), 2), float(input(" discount percent: ")))
    elif user_choice == 5:
        return f"everyone pays ${tip(round(float(input(" original price: ")), 2), float(input(" tip percent: ")), int(input(" amount of people: ")))}"
    else:
        return "invalid input"


#while loop to continuously run main function and stupid proof it
while True:
    try:
        print(main(int(input("""\nwhat would you like to do? type:
1 to see how many monthly deposits it takes to reach a goal
2 to calculate compound interest
3 to evenly calculate budget among several items
4 to calculate a discount
5 to calculate a tip
your answer here:
"""))))
    except ValueError:
        print("invalid input")