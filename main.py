'''
Day Trip Generator
Learning objective: Use and practice Python fundamentals, with an emphasis on Single Responsibility.
Technologies: Python
Project points (unweighted): /70
Project points (weighted): /10
Features: 
A. (5 points): As a developer, I want to make at least three commits with descriptive messages.
B. (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and 
   entertainments in their own separate lists.
C. (5 points): As a user, I want a destination to be randomly selected for my day trip.
D. (5 points): As a user, I want a restaurant to be randomly selected for my day trip.
E. (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip.
F. (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
G. (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of 
   transportation, and/or form of entertainment if I don’t like one or more of those things.
H. (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the 
   random selections.
I. (10 points): As a user, I want to display my completed trip in the console.
J. (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each 
   function should do just one thing!


'''

# A-----Make atleast 3 commits-----------

# B------Itenerary stored in lists----------

Destinations = ["The mall", "A food truck", "My place"]

Restaurants = ["A taco place", "A Spaghetti place", "My place"]

Transportations = ["Car", "Plane", "Enchanted eagle"]

Entertainments = ["Space Ghost Coast to Coast", "Feed pigeons in park", "Walking a dog"]

# C------Destination and Randomly reselect-----------




def user_destination(Destinations): 
    import random
    user_input = "NO"
    while user_input == "NO":
        destination = random.choice(Destinations)
        print(destination)
        user_input = input("Does this destination work for you?: ").upper()
        if user_input == "YES":
            return destination
            
destination = user_destination (Destinations)

# D ------Restaurants and Randomly reselect--------

def user_restaurant(Restaurants):
    import random
    user_input = "NO"
    while user_input == "NO":
        restaurant = random.choice(Restaurants)
        print(restaurant)
        user_input = input("Does this restaurant work for you?: ").upper()
        if user_input == "YES":
            return restaurant
            
restaurant = user_restaurant (Restaurants)

# E ------Transportation and Randomly reselect-----------

def user_transportation(Transportions):
    import random
    user_input = "NO"
    while user_input == "NO":
        transportation = random.choice(Transportions)
        print(transportation)
        user_input = input("Does this transportation work for you?: ").upper()
        if user_input == "YES":
            return transportation
            
transportation = user_transportation (Transportations)

# F --------Entertainment and Randomly reselect---------

def user_entertainment(Entertainments):
    import random
    user_input = "NO"
    while user_input == "NO":
        entertainment = random.choice(Entertainments)
        print(entertainment)
        user_input = input("Does this entertainment work for you?: ").upper()
        if user_input == "YES":
            return entertainment
            
entertainment = user_entertainment (Entertainments)

# G ----------------


# ----------------Print itenerary------------------------------


def user_statement (destination, restaurant, transportation, entertainment):
    statement = """ 
    For this day trip you have selected
    to make {} your destination. You will 
    be eating at {} and arriving by {}. 
    Entertainment will be provided by {}.""".format(destination, restaurant, transportation, entertainment)
    print (statement)

statement = user_statement (destination, restaurant, transportation, entertainment)

#-------------User confirmation--------------------

def user_confirmation ():
    confirmation = input("Would you like to confirm this trip? Yes or No ").upper()
    if confirmation == "YES":
        print("Enjoy your trip!")
    else:
        print("Sorry for your dissatisfaction")

confirmation = user_confirmation()


