
# making a function to handle user input data
def requestData():
    print("Welcome to our proprietary EV car selection programme, please insert the following information:")
    print("Option 1 : RM50,000 - RM100,000")
    print("Option 2 : RM100,000 - RM150,000")
    print("Option 3 : RM150,000 - RM200,000")
    print("Option 3 : RM200,000 or more")
    user_budget = int(input("Please choose the option of the desired budget range for the car  : "))
    if user_budget >=1 and user_budget <5:
        print("Budget accepted")
        print("Please specify the range of your desired EV following one of the options below")
        print("Option 1 : 200 - 300")
        print("Option 2 : 300 - 400")
        print("Option 3 : 400 - 500")
        print("Option 4 : 500 or more")
        user_range = int(input("Please choose an option : "))
        if user_range >=1 and user_range <5:
            print("Option accepted")
            print("Please specify whether the car has to be New or Used (second-hand) : ")
            print("Option 1 : New")
            print("Option 2 : Used")
            user_condition = input("Please choose an option: ")
            if user_condition == 1 or user_condition == 2:
                print("Option accepted")
                print("These are the brands that our company is connected to : ")
                print(car_brand)
                user_brand = str(input(("Please type a selected car brand within our database : "))).lower()
                for x in car_brand:
                    if x in car_brand:
                        print("Car brand is valid")
                        return user_budget, user_range, user_condition, user_brand
                    else:
                        print("Car brand is not valid within our database. Rerouting to main page. ")
                        start()
            else:
                print("Not a valid option, please choose a number between 1 to 2. Rerouting to main page.")
                start() 
        else:
            print("Not a valid option, please choose a number between 1 to 4. Rerouting to main page.")
            start()
    else:
        print("You can only type numbers, for the budget section. Rerouting to main page.")
        start()

def start():
    user_data = requestData()
    print(user_data)
# making the arrays for all the information
 
car_budget      = ["181000","",]
car_range       = ["629","",]
car_condition   = ["New","",]
car_brand       = ["Tesla", "Hyundai"]
car_description = ["Model 3", "Ioniq 5"]

start()