users = []

def register_user(username, password, card_type):
    valid_card_types = ['business', 'rewards', 'secured']
    if card_type.lower() not in valid_card_types:
        print(f"Invalid card type. Please choose from: {', '.join(valid_card_types)}.")
        return
    
    for user in users:
        if user['username'] == username:
            print("Username already exists. Please choose a different one.")
            return
    
    users.append({'username': username, 'password': password, 'card_type': card_type.lower(), 'balance': 0.0})
    print("User registered successfully!")

def login_user(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            print(f"Welcome, {username}! You are logged in with a {user['card_type']} card.")
            return user 
    print("Invalid username or password.")
    return None

def add_balance(user, amount):
    if amount <= 0:
        print("Amount to add must be greater than 0.")
        return
    user['balance'] += amount
    print(f"${amount:.2f} added to your balance. New balance: ${user['balance']:.2f}.")

def withdraw_balance(user, amount):
    if amount <= 0:
        print("Amount to withdraw must be greater than 0.")
        return
    if amount > user['balance']:
        print("Insufficient balance.")
        return
    user['balance'] -= amount
    print(f"${amount:.2f} withdrawn from your balance. New balance: ${user['balance']:.2f}.")

def check_balance(user):
    print(f"Your current balance is: ${user['balance']:.2f}")

def rewards(user):
    if user['card_type'] == 'business':
        print("You have earned 2% cashback on your purchases.")
    elif user['card_type'] == 'rewards':
        print("You have earned 1.5% rewards points on your purchases.")
    elif user['card_type'] == 'secured':
        print("You are eligible for a $10 bonus after your next payment.")
    else:
        print("No rewards available for your card type.")

def intro():
    print("Welcome to the Elite 101 Chat Bot!")
    username = input("What is your name?: ")
    print("Nice to meet you, " + username)
    age = input("How old are you?: ")
    print(f"Welcome {username}! Oh to be {age} again... How can I help you today?")
    
    current_user = None  

    while True:
        print("\nPlease choose from the following options: ")
        print("1. User Sign Up")
        print("2. User Login")
        print("3. Manipulate Balance")
        print("4. Rewards")
        print("5. Exit the conversation")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            username = input("What username would you like to register?: ")
            password = input("What password would you like to set?: ")
            card_type = input("What card type would you like to register for? (business, rewards, secured): ")
            register_user(username, password, card_type)

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            current_user = login_user(username, password)

        elif choice == "3":
            if current_user:
                print("\nBalance Manipulation Options:")
                print("1. Add Balance")
                print("2. Withdraw Balance")
                print("3. Check Balance")
                sub_choice = input("Enter the number of your choice: ")

                if sub_choice == "1":
                    amount = float(input("Enter the amount to add: "))
                    add_balance(current_user, amount)
                elif sub_choice == "2":
                    amount = float(input("Enter the amount to withdraw: "))
                    withdraw_balance(current_user, amount)
                elif sub_choice == "3":
                    check_balance(current_user)
                else:
                    print("Invalid option. Please try again.")
            else:
                print("You need to log in first.")

        elif choice == "4":
            if current_user:
                rewards(current_user)
            else:
                print("You need to log in first.")

        elif choice == "5":
            print("Thank you for using the Elite 101 Chat Bot. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

intro()