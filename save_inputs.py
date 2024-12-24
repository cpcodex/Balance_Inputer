import json

# Collect user input (example)
user_data = {}
user_data["name"] = input("Enter your name: ")
user_data["age"] = int(input("Enter your age: "))
user_data["city"] = input("Enter your city: ")

# Specify the file path
file_path = "user_data.json"

# Write to JSON file
try:
    with open(file_path, "w") as json_file:
        json.dump(user_data, json_file, indent=4)  # Use indent for pretty printing
    print(f"Data saved to {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
