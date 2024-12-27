import json
import os
from datetime import date, datetime

# Time variables
today = date.today()
now = datetime.now()

# Specify the file path
file_path = "user_data.json"


def data_inputs():
    # User Inputs for user database
    fname = input("Enter your first name: ").capitalize()
    lname = input("Enter your last name: ").capitalize()
    age = int(input("Enter your age: "))

    # Set Time variables
    tdate = today.strftime("%m/%d/%Y")
    input_time = now.strftime("%I:%M:%S %p")

    # Template user data
    user_data = {
        "first_name": fname,
        "last_name": lname,
        "age": age,
        "input_date": tdate,
        "input_time": input_time,
    }

    return user_data


def save_user_data(file_name):
    # Saves user data to JSON file

    # define data
    input_data = data_inputs()

    if os.path.exists(file_name):
        with open(file_name, "r") as json_file:
            try:
                data = json.load(json_file)  # Load existing JSON data
                if not isinstance(data, list):
                    data = []  # Reset to an empty list if data isn't an array
            except json.JSONDecodeError:
                data = []  # Reset to an empty list if the file content isn't valid JSON
    else:
        data = []  # Start with an empty list if the file doesn't exist

    # Append the new user data
    data.append(input_data)

    # Write the updated data back to the file
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)
    print(f"Data saved to {file_name}")
    return


def read_user_data(file_name):
    # read_user_data being utilized user user_data_list, reads file contents

    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as json_file:
                data = json.load(json_file)  # Load JSON data into a Python list
                print("All User Data:")
                for user in data:
                    print(user)

                # access specific data if data exists
                if data:
                    last_user = data[-1]
                    print("\nLast user's first name:", last_user["first_name"])
                    print("Last user's last name:", last_user["last_name"])
                return data
        except FileNotFoundError:
            print("File not found.")
            return []
        except json.JSONDecodeError:
            print("Error decoding JSON data.")
            return []
    else:
        print("Error has occured in reading")
    return []


fix = input("Would you like to read or save this data? S or R ").capitalize()

if fix == "S":
    # Save user data
    save_user_data(file_path)
elif fix == "R":
    # Read user data
    read_user_data(file_path)
else:
    print("No need to read this.")

# # Set loop to true, False breaks/closes program
# data_loop = True
# while data_loop == True:
#     # Loop through inputs to choose action

#     # User Input
#     user_input = "What would you like to do? "

#     # check user_input
#     if user_input == "A":
#         # Add user data
#         pass
#         #  User Inputs for user database
#         # fname = input("Enter your first name: ").capitalize()
#         # lname = input("Enter your last name: ").capitalize()
#         # age = int(input("Enter your age: "))

#     elif user_input == "R":
#         # Read user data

#         pass

#     elif user_input == "C":
#         # Call specific data

#         pass

#     else:
#         print(
#             "Invalid input, please try again.\n",
#             "You may choose between:\n",
#             '- "A" to add data\n',
#             '- "R" to read data\n',
#             '- "C" to call specific data\n',
#             '- "Q" to quit the program\n',
#         )
