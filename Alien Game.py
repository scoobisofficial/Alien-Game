import random 
# Welcome to the ALIEN GAME
# The beginning steps and comments are scaffolded below, but you will need to look at your directions on schoology for the rest
print("Welcome to the ALIEN GAME!")
print("You have stolen a UFO to make your way across outer space.")
print("The aliens want their UFO back and are chasing you down! Survive and out run the Aliens!")
print()
# Create a boolean variable called done and set to False
done = False
# Create variables for miles traveled, thirst, and tiredness. Set these to zero
milesTraveled = 0
thirst = 0
tiredness = 0
# Create a variable for the distance the aliens have traveled and set it to -20
alienDistance = -20
# Create and set an initial number of drinks in the water bottle - start with 3
waterDrinks = 3
# Create a while loop that will keep looping while done is False
while done == False:
    print("A. Drink from your water bottle.")
    print("B. Speed up at MODERATE speed.")
    print("C. Speed up at FULL speed")
    print("D. Rest.")
    print("E. Status Check")
    print("Q. Quit.")
    print()
    usersChoice = input("What do you want to do? Select the letter of your choice: ")
    #Quit option!!
    if usersChoice.upper() == 'Q':
        done = True
        print("You Quit!!")
    # Status Check
    elif usersChoice.upper()== 'E':
        print("A status check has been requested.")
        print("Your current distance is",milesTraveled,"miles.")
        print("Drinks in water bottle:",waterDrinks,)
        print("The Aliens are",alienDistance,"miles behind you!")
        print("Thirst is",thirst,)
        print()
    #Resting
    elif usersChoice.upper() == 'D':
        tiredness = 0
        alienDistance += (random.randrange(7, 14))
        print("You took a nap. During your slumber, the aliens have caught up by",alienDistance,"miles")
    #Option A
    elif usersChoice.upper() == 'A':
        if waterDrinks >= 1:
            thirst = 0
            waterDrinks -= 1
            print("The water feels refreshing. Your thirst has been reset to 0.")
            print("Returning to the Main Menu.")
            print()
        else:
            print("You have no water")
    #Choice B
    elif usersChoice.upper() == 'B':
        moderateSpeedMiles = (random.randrange(5, 12))
        milesTraveled += moderateSpeedMiles
        thirst += 0.5
        tiredness += 1
        alienDistance += (random.randrange(6, 12))
        print("You have traveled",milesTraveled,"miles.")
        print()
    #FULL SPEED!!
    elif usersChoice.upper() == 'C':
        fullSpeedMiles = (random.randrange(10,20))
        milesTraveled += fullSpeedMiles
        thirst += 1
        tiredness += (random.randrange(1,2))
        alienDistance += (random.randrange(8, 14))
        print("You have traveled",milesTraveled,"miles.")
        print()
    # Thirst Mechanic
    if 4 < thirst < 6:
        print("You are thirsty")
    elif thirst >=6:
        print("You fainted of thirst and the aliens caught up!")
        done = True
    #Tiredness Mechanic
    if 5 < tiredness < 8:
        print("You are getting tired.")
    elif tiredness >=8:
        print("You fell asleep while flying the UFO and the aliens caught up!")
        done = True
    # Aliens got player
    if alienDistance == milesTraveled:
        print("The Aliens caught you...")
        done = True
    elif alienDistance <= 15:
        print("The aliens are getting close. RUN!")
    #200 Miles
    if milesTraveled >= 200:
        print("You Win!!! But, are you alive?")
        done = True
