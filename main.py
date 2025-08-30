from services.Authentication import Authentication

print("Welcome to Library Mangement System!")
print("====================================")

print("\nMenu: ")
print("------")
print("1. Log in")
print("2. Exit\n")

while True :
    choice = int(input("Please Enter your Choice: "))

    if choice == 2 :
        print("GoodBye:)")
        break

    elif choice == 1 :
        authentication = Authentication()
        username = input("Please Enter your Username: ")
        password = input("Please Enter your Password: ")
        authentication.login(username, password)
        break
    else :
        print("Invalid Choice, Please try again.")