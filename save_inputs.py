import json

# User Inputs
fname = input("Enter your name: ")
lname = input("Enter your name: ")
age = input("Enter your name: ")
tdate = input("Enter your name: ")
curr_time = input("Enter your name: ")

# Collect user input (example)
user_data = {
    "fname": fname,
    "lname": lname,
    "age": age,
    "date": tdate,
    "curr_time": curr_time,
}

# Specify the file path
file_path = "user_data.json"

# Write to JSON file
try:
    with open(file_path, "a") as json_file:
        json.dump(user_data, json_file, indent=4)  # Use indent for pretty printing
    print(f"Data saved to {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
