import json
import os
from datetime import date, datetime

# Time variables
today = date.today()
now = datetime.now()

# Specify the file path
file_path = "user_data.json"


def save_user_data(file_name, user_data):
    # Saves user data to JSON file

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
    data.append(user_data)

    # Write the updated data back to the file
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)
    print(f"Data saved to {file_name}")


def read_user_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)  # Load JSON data into a Python list
            return data
    except FileNotFoundError:
        print("File not found.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
        return []


# User Inputs for user database
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = int(input("Enter your age: "))

# Set Time variables
tdate = today.strftime("%m/%d/%Y")
curr_time = now.strftime("%I:%M:%S %p")

# Collect user input
user_data = {
    "first_name": fname,
    "last_name": lname,
    "age": age,
    "date": tdate,
    "curr_time": curr_time,
}

# Define User Data List
user_data_list = read_user_data(file_path)

# Check and loop through contents
if user_data_list:
    print("All User Data:")
    for user in user_data_list:
        print(user)

    # Access specific data
    # print("\nFirst user's first name:", user_data_list[5]["lname"])
else:
    print("No data available.")

save_user_data(file_path, user_data)
# Write to JSON file
# try:
#     with open(file_path, "w") as json_file:
#         json.dump(user_data, json_file, indent=4)  # Use indent for pretty printing
#     print(f"Data saved to {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")
