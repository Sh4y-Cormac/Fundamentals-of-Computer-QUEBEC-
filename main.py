
def requestData(user_budget, user_range):
    print("Welcome to our proprietary EV car selection programme, please insert the following information:")
    user_budget = input("Please enter desired budget for your car (use only numbers) : ")
    if user_budget.isdigit():
        print("Budget accepted")
        print("Please specify the range of your desired EV following one of the options below")
        print("Option 1 : 200 - 300")
        print("Option 2 : 300 - 400")
        print("Option 3 : 400 - 500")
        print("Option 4 : 500 or more")
        user_range = input("Please choose an option : ")
        if user_range <1 and user_range <5:
            print("Option accepted")
            print("Please choose if the desired car is  or used?")
        else:
            print("Not a valid option, please choose a number between 1 to 4. Rerouting to main page.")
    else:
        print("You can only type numbers, for the budget section. Rerouting to main page.")
        requestData(0)

# making the arrays for all the information
 
car_budget      = ["181000","",]
car_range       = ["629","",]
car_condition   = ["New","",]
car_brand       = ["Tesla Model 3", "Hyundai Ioniq 5 Lite"]
