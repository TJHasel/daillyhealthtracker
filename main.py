from classes import User
from workout_list import *
import time
from datetime import date
import os

#getting date from datetime mod
print("---------------------------------------------------------")
print("\n Daily Health Tracker \n")
print("---------------------------------------------------------")
today = date.today()
time.sleep(1)

#loop to continue questions if errors present
while True:
    #ask questions for curr. weight and ideal weight
    try:
        ask_current_weight = int(input("Current weight (in lbs): " + "\n"))
        print("---------------------------------------------------------")
        time.sleep(1)

        ask_ideal_weight = int(input("Ideal weight (in lbs): " + "\n"))

    except ValueError:
        print("Please start over.. only enter whole numeric values for weight")
    #continue with other questions
    else: 
        print("---------------------------------------------------------")
        time.sleep(1)
        ask_calories_burned = input("Exercises and calories burned, "
        "sep. by a comma (ie. running, 150, cycling, 300): " + "\n").split(',')

        print("---------------------------------------------------------")
        time.sleep(1)

        ask_food_items = input("Food items and calories per food item, " 
        "sep. by a comma (ie. tacos, 300, tea, 50): " + "\n").split(',')

        print("--------------------------------------------------------- \n")
        time.sleep(3)

        #tuple to store input data and be used later in functions
        saved_inp_data = tuple((today,ask_current_weight,
        ask_ideal_weight,ask_calories_burned,ask_food_items))
        break

def daily_totals(x,y):
    '''
    daily_totals to take in input from above, convert list 
    values to a dictionary and run through the class 
    method User.cal_calculation() for differnce in 
    intake v. ideal intake

    Variables:

    new_dict_exc - represents a dictionary pulling list 
    values (exercise, cals burned)
    new_dict_food - represents a dictionary 
    pulling list values (food, cals taken in)
    sum_of_exc - sum of values in exercise dictionary
    sum_of_food - sum of values in food dictionary
    user1 - to represent the user1 from the class import

    Returns:

    totals of caloric intake for the day and what the difference was 
    between that, exercise cals burned, and ideal target

    '''
    #splitting lists into dictionaries by key, value
    new_dict_exc = {x[item]: int(x[item + 1]) for item in range(0, len(x), 2)}

    new_dict_food = {y[item]: int(y[item + 1]) for item in range(0, len(y), 2)}
    #get some of the values
    sum_of_exc = sum(new_dict_exc.values())

    sum_of_food = sum(new_dict_food.values())

    user1 = User(currentweight=saved_inp_data[1], 
    idealweight=saved_inp_data[2], name="")
    #pass outputs from this func. through cal_calculation method in class
    return user1.cal_calculation(sum_of_food,sum_of_exc)

def recommender():
    '''
    Based on the difference between user's current weight and ideal weight,
    will recommend certain exercise types based on that difference.
    cardio v. strength exercises.

    Variables:
    counter - ticker used in the for loop to track how 
    many times the loop has been ran

    Returns:

    either strength exercises from sets in workout_list file
    according to the difference in the user's current
    and ideal weight.

    '''

    counter = 0
    #loop through cardio set
    for item in cardio_set:
        counter = counter + 1
        #condition if current weight is 10% over ideal
        if ask_current_weight >= ask_ideal_weight * 1.1 and counter < 5:
            print(item)
        else: 
            #loop through strength set
            for item2 in strength_set:
                counter = counter + 1
                if counter < 6:
                    print(item2)

def open_file():
    
    '''
    writes current date, exercises, calories burned from each, food items, 
    and calories from food.

    Variables:

    log - stores the file to wrie to 

    Returns:

    writes to the daily_log file, returns nothing

    '''
    user1 = User(currentweight=ask_current_weight, 
    idealweight=ask_ideal_weight, name="")

    dir = os.path.dirname(__file__) 
    path = "daily_log1.txt"
    abs_file_path = os.path.join(dir, path)
    #file

    file =  open (abs_file_path, "a") 
        #joining list into string and pass through weight_grabber method
    file.write(" ".join(user1.weight_grabber(saved_inp_data[0],
    saved_inp_data[1])) + "\n")
        #write string of exercises and food items to file
    file.write("Exercises: {}  \n".format(" ".join(saved_inp_data[3])) +
    "Food Items: {} \n\n".format(" ".join(saved_inp_data[4])))
    
    file.close() 

if __name__ == '__main__':
    
    while True:
        #attempt to run daily_totals() with user input
        try:
            print(daily_totals(ask_calories_burned,ask_food_items))
            break
        #if VE, IE raised, ask these questions again
        except (ValueError, IndexError):
            print("Oops.. Make sure to follow the format (x,cals) \n")
            ask_calories_burned = input("Exercises and calories burned, "
            "sep. by a comma: " + "\n").split(',')

            print("------------------------------------------------------")
            time.sleep(1)

            ask_food_items = input("Food items and calories per food item, " 
            "sep. by a comma: " + "\n").split(',')

            print("-------------------------------------------------------\n")
            time.sleep(3)

#call function to write to daily_log
open_file()

print("\n" + "=> Please check the Daily Log for a record of your weights, "
"workouts, and calorie intake" + "\n")

print("** extra tip: try one or more of these suggested exercises "
"for tomorrow ** " + "\n")
time.sleep(1)

#call to display recommended workouts
print("--------")
recommender()
print("--------")















