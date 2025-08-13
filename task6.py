def register_user(users):
    print("=== Register User ===")
    username = input("Enter a new username: ").strip()
    if username in users:
        print("Username already exists. Please try a different one.")
        return
    password = input("Enter a new password: ").strip()
    users[username] = password
    print("Registration successful!\n")

def login_user(users):
    print("=== Login User ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users and users[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Invalid username or password.\n")

def main():
    users = {}
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            register_user(users)
        elif choice == '2':
            login_user(users)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
