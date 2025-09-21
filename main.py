# importing quality of life systems e.g clearscreen and timewait
import os
import time

DB_FILE = "users.txt"

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
2
    if u not in users:
        print("Invalid account. Please sign up first.")
        return

    if users[u] == p:
        print(f"Login Succeed! Welcome, {u}.")
        # TERUS MASUK CODE UMAR
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

# function to start the user input programme
def start():
    user_data = requestData()
    print(user_data)

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
car_budget      = ["181000","",]
car_range       = ["629","",]
car_condition   = ["New","",]
car_brand       = ["tesla", "hyundai"]
car_description = ["Model 3", "Ioniq 5"]

start()