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



pseudocode

create lists of the 4 parameter lists

functions to randomly select from lists
    ask user if they want to re-select each item

confirm the trip

display completed trip to console


'''

# A----------------

# B----------------

Destinations = ["The mall", "Food truck", "My place"]

Restaurants = ["Taco place", "Spaghetti place", "My place"]

Transportations = ["Car", "Plane", "Eagle"]

Entertainments = ["Space Ghost Coast to Coast", "Feed pigeons in park", "Walk dog"]

# C-----------------




def user_destination(Destinations):
    import random
    user_input = "NO"
    while user_input == "NO":
        destination = random.choice(Destinations)
        print(destination)
        user_input = input("Does this destination work for you?").upper()
        if destination == "YES":
            return destination
            
destination = user_destination (Destinations)

# D ----------------

def user_restaurant(Restaurants):
    import random
    user_input = "NO"
    while user_input == "NO":
        restaurant = random.choice(Restaurants)
        print(restaurant)
        user_input = input("Does this restaurant work for you?").upper()
        if restaurant == "YES":
            return restaurant
            
restaurant = user_restaurant (Restaurants)

# E -----------------

def user_transportation(Transportions):
    import random
    user_input = "NO"
    while user_input == "NO":
        transportation = random.choice(Transportions)
        print(transportation)
        user_input = input("Does this transportation work for you?").upper()
        if transportation == "YES":
            return transportation
            
transportation = user_transportation (Destinations)

# F -----------------

def user_entertainment(Entertainments):
    import random
    user_input = "NO"
    while user_input == "NO":
        entertainment = random.choice(Entertainments)
        print(entertainment)
        user_input = input("Does this entertainment work for you?").upper()
        if entertainment == "YES":
            return entertainment
            
entertainment = user_entertainment (Entertainments)

# G ----------------

def trip_selection (destination, restaurant, transportation, entertainment):
    day_trip = [destination, restaurant, transportation, entertainment]
    return day_trip

trip_list = trip_selection (destination, restaurant, transportation, entertainment)


# ----------------------------------------------


def user_statement (destination, restaurant, transportation, entertainment):
    statement = """ 
    For this day trip you have selected
    to make {} your destination. You will 
    be eating at {} and arriving by {}. 
    Entertainment will be provided by {}.""".format(destination, restaurant, transportation, entertainment)
    print (statement)

statement = user_statement (destination, restaurant, transportation, entertainment)

#---------------------------------

def user_confirmation ():
    confirmation = input("Would you like to confirm this trip?")
    if confirmation == "YES":
        print("Enjoy your trip!")
    else:
        print("Sorry for your dissatisfaction")

confirmation = user_confirmation()



# def user_destination():
#     import random
#     destination = random.choice(Destinations)
#     return destination

# # D ----------------

# def user_restraunt():
#     import random
#     restaurant = random.choice(Restaurants)
#     return restaurant

# # E -----------------

# def user_transportation():
#     import random
#     transportation = random.choice(Transportations)
#     return transportation

# # F -----------------

# def user_entertainment():
#     import random
#     entertainment = random.choice(Entertainments)
#     return entertainment

# # G ----------------

# def trip_selection ():
#     day_trip = [user_destination(), user_restraunt(), user_transportation(), user_entertainment()]
#     return day_trip


# H -----------------
#













def user_preference (destination, restaraunt, transportation, entertainment):
    statement = """ 
    I have an idea for a day trip!!!!!
    You can go to {} for a destination
    Then for dinner you can go to {}
    To get there, you can take {}
    and for entertainment, you can {}""".format (destination, restaraunt, transportation, entertainment)
    Trip_assessment = [destination, restaraunt, transportation, entertainment]
    print (statement)
    return Trip_assessment



# def user_verification ():
#     change_list=[]
#     Verification = input("Would you like to make any changes to the trip? Yes or No").upper()
#     if Verification == "NO":
#         print ("Enjoy your day trip!")
#     else:
#         Verification == "YES"
#         print ("Let's make some changes")
#         destination= input("Would you like to change the destination?").upper()
#         change_list.append(str(destination))
#         restaurant = input("Would you like to change the restaurant?").upper()
#         change_list.append(str(restaurant))
#         transportation = input("Would you like to change the transportation?").upper()
#         change_list.append(str(transportation))
#         entertainment = input("Would you like to change the entertainment?").upper()
#         change_list.append(str(entertainment))
#     return change_list





# Trip_assessment = user_preference(user_destination(), user_restraunt(), user_transportation(), user_entertainment())
# bill = user_verification()
# print(bill)






# 
# 
# 
# 
# 
# 
# 
# 
#  def user_preference (destination, restaraunt, transportation, entertainment):
#     statement = """ 
#     I have an idea for a day trip!!!!!
#     You can go to {} for a destination
#     Then for dinner you can go to {}
#     To get there, you can take {}
#     and for entertainment, you can {}""".format (destination, restaraunt, transportation, entertainment)
#     Trip_assessment = [destination, restaraunt, transportation, entertainment]
#     print (statement)
#     return Trip_assessment
    
    
# def user_verification ():
#     Verification = input("Would you like to make any changes to the trip? Yes or No").upper()
#     if Verification == "NO":
#         print ("Enjoy your day trip!")
#     else:
#         Verification == "YES"
#         print ("Let's make some changes")

# def user_changes (destination, restaurant, transportation, entertainment):
#     List = []
#     List.append(destination)
#     List.append(restaurant)
#     List.append(transportation)
#     List.append(entertainment)
#     return List



# def destinations_change ():
#     print("The destination?")
#     destination = input("").upper
#     return destination
    
# def restaurants_change ():
#     print("The restaurant?")
#     restaurant = input("").upper
#     return restaurant

# def destinations_change (): 
#     print("The transportation?")
#     transportation = input("").upper
#     return transportation

# def entertainment_change ():
#     print("The entertainment?")
#     entertainment = input("").upper
#     return entertainment



# user_preference(user_destination(), user_restraunt(), user_transportation(), user_entertainment())
# user_verification ()
# user_changes ()

