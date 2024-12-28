# NOTE: continue adding new methods and features to the data base.
# TODO: create search by key for accessing database
import json
import os
from datetime import date, datetime

# Specify the file path
file_path = "user_data.json"


def data_inputs():
    # User Inputs for user database
    fname = input("Enter your first name: ").capitalize()
    lname = input("Enter your last name: ").capitalize()
    age = int(input("Enter your age: "))

    # Set Time variables
    today = date.today()
    now = datetime.now()
    tdate = today.strftime("%m/%d/%Y")
    input_time = now.strftime("%I:%M:%S %p")

    # Template user data
    user_data = {
        "firstname": fname,
        "lastname": lname,
        "age": age,
        "date": tdate,
        "time": input_time,
    }

    return user_data


def save_user_data(file_name):
    # Saves user data to JSON file, call save_user_data(file_path)

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
    return []


def read_user_data(file_name):
    # read user data, call read_user_data(file_path)

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
                    print(
                        "\nLast user:",
                        last_user["firstname"],
                        last_user["lastname"],
                    )
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


def search_user_data(file_name, search_key):
    # Search for a specific key in user data

    if os.path.exists(file_name):
        with open(file_name, "r") as json_file:
            try:
                data = json.load(json_file)

                # prepare search list
                results = []
                for user in data:
                    if search_key in user:
                        results.append({search_key: user[search_key]})

                if results:
                    print(f"Found {search_key}:")
                    for index, result in enumerate(results, start=1):
                        print(f"{index}: {result.get(search_key)}")

                else:
                    print(f"No users found with the key '{search_key}'.")
                return results

            except json.JSONDecodeError:
                print("Error decoding JSON data.")
                return []
    else:
        print("File not found or error in reading.")
        return []


# NOTE debugging NOTE
# ============================================================================= #
# while True:
#     fix = input(
#         "Would you like to read, lookup, save, or quit this data? S, L, Q, or R "
#     ).capitalize()

#     if fix == "S":
#         # Save user data
#         save_user_data(file_path)
#     elif fix == "R":
#         # Read user data
#         read_user_data(file_path)
#     elif fix == "L":
#         # search key in user data
#         search_key = input("Which would you like to search for? ").strip().lower()
#         search_user_data(file_path, search_key)
#     elif fix == "Q":
#         # Read user data
#         print("Exiting input debugger...")
#         break
#     else:
#         print("ERROR")
