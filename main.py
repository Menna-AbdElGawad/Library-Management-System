from services.Authentication import Authentication
from core.Policies import Policies

print("Welcome to Library Mangement System!")
print("====================================")

def main():
    while True :
        print("\n===== Main Menu =====")
        print("------")
        print("1. Sign Up (as a Customer)")
        print("2. Log in")
        print("3. Policies")
        print("0. Exit\n")

        choice = int(input("Please Enter your Choice: "))

        if choice == 0 :
            print("GoodBye:)")
            break

        elif choice == 1 :
            auth = Authentication()
            auth.signup()
            break

        elif choice == 2:
            auth = Authentication()
            auth.login()
            break

        elif choice == 3:
            policy = Policies()
            policy.show_policies()
        
        else :
            print("Invalid Choice, Please try again.")

if __name__ == "__main__":
    main()