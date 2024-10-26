excel_file = "user_data.xlsx"

import pandas as pd
import os

excel_file = "user_data.xlsx"

def add_user():
    name = input("Enter your name : ")
    email = input("ENter your email: ")
    phone  = input("ENter your phone: ")

    if not os.path.exists(excel_file):
        df = pd.DataFrame(columns=["Name","Email","Phone"])
        df.to_excel(excel_file, index=False)

    df = pd.read_excel(excel_file)
    new_data = pd.DataFrame({"Name" : [name], "Email": [email], "Phone":[phone]})
    df = pd.concat([df, new_data], ignore_index=True)

    df.to_excel(excel_file, index=False)
    print("User added Successfully")

def display_users():
    if os.path.exists(excel_file):
        df = pd.read_excel(excel_file)
        if df.empty:
            print("No users found.")
        else:
            print(df)
    else:
        print("Users No found.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add USer:")
        print("2. Display users")
        print("3. Exit")

        choice  =  input("ENter your choice: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            display_users()
        elif choice == "3":
            print("Exiting Program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()