from password_manager import PasswordManager

def main():
    master_key = input("Enter master key (for encryption): ")
    pm = PasswordManager(master_key)

    while True:
        print("\n🔐 Password Manager")
        print("1. Check Strength")
        print("2. Generate Password")
        print("3. Strengthen My Password")
        print("4. View Stored Passwords")
        print("5. Exit")

        choice = input("Choice: ")

        if choice == "1":
            pwd = input("Enter password: ")
            strength, feedback = pm.check_strength(pwd)
            print("Strength:", strength)
            for f in feedback:
                print("-", f)
                save = input("Do you want to save this password? (y/n): ").lower()
if save == "y":
    pm.save_password(pwd)
    print("Password saved securely.")

        elif choice == "2":
            pwd = pm.generate_password()
            print("Generated:", pwd)

            if input("Save it? (y/n): ").lower() == "y":
                pm.save_password(pwd)

        elif choice == "3":
            base = input("Enter base password: ")
            strong = pm.strengthen_password(base)
            print("Stronger version:", strong)
            save = input("Do you want to save this password? (y/n): ").lower()
if save == "y":
    pm.save_password(strong)
    print("Password saved securely.")

        elif choice == "4":
            print("Stored Passwords:")
            for p in pm.load_passwords():
                print("-", p)

        elif choice == "5":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
