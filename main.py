# importing quality of life systems e.g clearscreen and timewait
import os
import time

DB_FILE = "users.txt"

# function to start the user input programme
def start():
    global user_brand, user_budget, user_condition, user_range

    user_data = requestData()

    #tuple unpacking
    user_budget, user_range, user_condition, user_brand = user_data

    matches = find_matching_cars(user_budget, user_range, user_condition, user_brand)
    print_matches(matches)



# making a function to handle user input data
def requestData():
    print("Welcome to our proprietary EV car selection programme, please insert the following information:")
    print("Option 1 : RM50,000 - RM100,000")
    print("Option 2 : RM100,000 - RM150,000")
    print("Option 3 : RM150,000 - RM200,000")
    print("Option 4 : RM200,000 or more")
    user_budget = int(input("Please choose the option of the desired budget range for the car  : "))
    transition()
    if user_budget >=1 and user_budget <5:
        print("Budget accepted")
        print("Please specify the range of your desired EV following one of the options below")
        print("Option 1 : 200 - 300")
        print("Option 2 : 300 - 400")
        print("Option 3 : 400 - 500")
        print("Option 4 : 500 or more")
        user_range = int(input("Please choose an option : "))
        transition()
        if user_range >=1 and user_range <5:
            print("Option accepted")
            print("Please specify whether the car has to be New or Used (second-hand) : ")
            print("Option 1 : New")
            print("Option 2 : Used")
            user_condition = int(input("Please choose an option: "))
            transition()
            if user_condition == 1 or user_condition == 2:
                print("Option accepted")
                print("These are the brands that our company is connected to : ")
                print(car_brand)
                user_brand = str(input(("Please type a selected car brand within our database : "))).lower()
                # loops through the car brand list to see if the selected brand is valid.
                for x in car_brand:
                    if user_brand in car_brand:
                        print("Car brand is valid")
                        return user_budget, user_range, user_condition, user_brand
                    else:
                        print("Car brand is not valid within our database. Rerouting to main page. ")
                        error()
                        start()
            else:
                print("Not a valid option, please choose a number between 1 to 2. Rerouting to main page.")
                error()
                start() 
        else:
            print("Not a valid option, please choose a number between 1 to 4. Rerouting to main page.")
            error()
            start()
    else:
        print("You can only type numbers, for the budget section. Rerouting to main page.")
        error()
        start()



#adds a QoL transition to improve customer experience
def transition():
    os.system('cls')
    print("----------------")
    time.sleep(0.1)

#specific transition for errors so the customer has time to see what the customer did wrong. 
def error():
    time.sleep(3)
    transition()


# making the arrays for all the information 
car_brand = ["tesla", "hyundai", "byd", "proton", "bmw"]


#Cars List Dictionary 
CARS = [
    {"brand": "tesla", "model": "Model 3", "price": 181000, "range": 629, "condition": "new" },
    {"brand": "tesla", "model": "Model 3", "price": 140000, "range": 580, "condition": "used" },
    {"brand": "hyundai", "model": "IONIQ 5", "price": 199888, "range": 504, "condition": "new" },
    {"brand": "hyundai", "model": "IONIQ 5", "price": 143888, "range": 300, "condition": "used" },
    {"brand": "byd", "model": "Seal", "price": 171800, "range": 650, "condition": "new" },
    {"brand": "byd", "model": "Seal", "price": 120000, "range": 570, "condition": "used" },
    {"brand": "proton", "model": "e.Mas7", "price": 109800, "range": 345, "condition": "new" },
    {"brand": "proton", "model": "e.Mas7", "price": 105800, "range": 345, "condition": "used" },    
    {"brand": "bmw", "model": "i4", "price": 294800, "range": 500, "condition": "new" },
    {"brand": "bmw", "model": "i4", "price": 198000, "range": 483, "condition": "used" },
]

#assigning output requirement numbers with their respective bounds
def budget_ranges(option: int):
    if option == 1: return (50000, 100000)
    if option == 2: return (100000, 150000)
    if option == 3: return (150000, 200000)
    if option == 4: return (200000, float("inf"))
    return (0, float("inf"))

def travel_ranges(option: int):
    if option == 1: return 200
    if option == 2: return 300
    if option == 3: return 400
    if option == 4: return 500
    return 0

def condition_of_car(option: int):
    return "New" if option == 1 else "Used"

#go through the car dictionary and find a car based on the requirement
def find_matching_cars(user_budget, user_range, user_condition, user_brand):
    low, high = budget_ranges(user_budget)
    rmin = travel_ranges(user_range)
    cond = condition_of_car(user_condition)

    matches = []
    for car in CARS:
        if (car["brand"].lower() == user_brand.lower()
            and car["condition"].lower() == cond.lower()
            and low <= car["price"] <= high
            and car["range"] >= rmin):
            matches.append(car)
    return matches

#car found yes or no
def print_matches(matches):
    if not matches:
        transition()
        print("\nSorry, no cars match your requirements.\n")
        choice = input("Would you like to see our recommendation closest to your requirements? (Yes/No)\n").lower()
        clear_screen()

        if choice == "no":
            new_budget, new_range, new_condition, new_brand = requestData()
            new_matches = find_matching_cars(new_budget, new_range, new_condition, new_brand)
            print_matches(new_matches)
            return
        elif choice == "yes":  
            clear_screen()
            print("\nThese are our recommended choices!\n")
            for car in CARS:
                if ( car['brand'] == user_brand
                    or  car['condition'] == condition_of_car(user_condition)
                    or car['range'] >= travel_ranges(user_range)
                    or (budget_ranges(user_budget)[0] <= car['price'] <= budget_ranges(user_budget)[1])
                ):
                    print(f"- {car['brand'].title()} {car['model']} | RM{car['price']:,} | {car['range']} km | {car['condition']}")
    else:
        clear_screen()
        print("\nWe found a match based on your requirement!:\n")
    for car in matches:
        transition()
        print(f"- {car['brand'].title()} {car['model']} | RM{car['price']:,} | {car['range']} km | {car['condition']}")
    print()

    print("\nDo you want to choose another option?(yes/no)\n")
    loop = input().lower()
    clear_screen()
    
    if loop == "yes":
        new_budget, new_range, new_condition, new_brand = requestData()
        new_matches = find_matching_cars(new_budget, new_range, new_condition, new_brand)
        print_matches(new_matches)
        return
    
    elif loop == "no":
        main()
        clear_screen()
        return
    
    else: print("Invalid input")
    time.sleep(2)
    clear_screen()
    start()
    return


# ----------------- Utility -----------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ensure_db():
    try:
        open(DB_FILE, "x").close()  # create file kalau tak ada
    except FileExistsError:
        pass

def load_users():
    users = {}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                u, p = line.split(":", 1)
                users[u] = p
    return users

def save_user(username, password):
    with open(DB_FILE, "a", encoding="utf-8") as f:
        f.write(f"{username}:{password}\n")

# ----------------- Features -----------------
def sign_up():
    print("[ SIGN UP ]")
    u = input("Enter username: ").strip()
    p = input("Enter password: ").strip()

    users = load_users()
    if u in users:
        print("Username already exists. Please try again.")
    else:
        save_user(u, p)
        print("Registration successful! Please login with your new account.")

def log_in():
    print("[ LOGIN ]")
    u = input("Enter username: ").strip()
    p = input("Enter password: ").strip()

    users = load_users()

    if u not in users:
        print("Invalid account. Please sign up first.")
        return

    if users[u] == p:
        print(f"Login Succeed! Welcome, {u}.")
        # TERUS MASUK CODE UMAR
        print("\n")
        print("----------------")
        start()            # <--- panggil function umar 
        return
    else:
        print("Password is incorrect.")


# ----------------- Banner -----------------
def print_banner():
    print(r"""
    __        __   _                            _         
    \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   
    \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  
    \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | 
     \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  
    """)
    print("        Welcome to EV Dealership\n")

# ----------------- Main Loop -----------------
def main():
    ensure_db()
    while True:
        clear_screen()
        print_banner()
        print("Do you want to log in or sign up?")
        print("1) log in")
        print("2) sign up")
        print("3) exit")
        choice = input("Choose (1/2/3): ").strip()

        clear_screen()

        if choice == "1":
            log_in()
            input("\nPress Enter to return to main menu...")
        elif choice == "2":
            sign_up()
            input("\nPress Enter to return to main menu...")
        elif choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid choice.")
            input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main()
