# NOTE: Note-bar is used to pick up where left off in previous session
# TODO: Finished balance history, continue implementing data collection, access, and cleanup code; reconsider how we store and access data.
from datetime import date, datetime

today = date.today()
now = datetime.now()


class Deposit:
    def __init__(self, dol, cts):
        self.dollars = dol
        self.cents = cts

    def __str__(self):
        return "You deposited ${}.{:02} to your total balance.".format(
            self.dollars, self.cents
        )


def sep_acct(val):
    # Function to create box around output
    print("=" * 45)
    print(val)
    print("=" * 45)


def date():
    # Todays date
    formatted_date = today.strftime("%m/%d/%Y")
    formatted_time = now.strftime("%I:%M:%S %p")
    print("Today is:", formatted_date)
    print("It is currently:", formatted_time)


def data_format():
    # Format data for file
    user_data["first_name"] = input("Enter your First Name: ").capitalize()
    user_data["last_name"] = input("Enter your Last Name: ").capitalize()
    user_data["age"] = int(input("Enter your age: "))
    user_data["date"] = today.strftime("%m/%d/%Y")
    user_data["time"] = now.strftime("%I:%M:%S %p")


def write_text():
    # Write file into txt file

    # open user_data file
    f = open("user_data.txt", "a")
    # Write data_format Dictionary to file
    f.write(f"{str(user_data)}\n")
    # write inputs to File
    f.write(f"Balance: ${tot_dollars}\n")
    f.close()


def read_file():
    read_file = input('Do you wish to read the saved file? "Yes" or "No" ').capitalize()

    if read_file == "Yes":
        # Read file
        fr = open("user_data.txt", "r")
        print(fr.read())
    elif read_file == "No":
        print("No problem, the file was saved to your directory!")
    else:
        print("Error reading file")


def last_bal():
    bal_input = input(
        'Do you wish to read the previous balance? "Yes" or "No" '
    ).capitalize()

    if bal_input == "Yes":
        fr = open("user_data.txt", "r")
        lines = fr.readlines()
        last_bal = lines[-1]
        print(last_bal)
    elif bal_input == "No":
        print("No problem, the file was saved to your directory!")
    else:
        print("Error reading file")


def bal_history():
    bal_hist = input(
        'Do you want to view your balance history? "Yes" or "No" '
    ).capitalize()

    if bal_hist == "Yes":
        fr = open("user_data.txt", "r")
        lines = fr.readlines()
        for i in range(1, len(lines), 2):
            print(lines[i].rstrip("\n"), user_data["date"])
    elif bal_hist == "No":
        print("No problem, the file was saved to your directory!")
    else:
        print("Error reading file")


# Print date
date()
# User Data Dictionary
user_data = {}
# Set app to true
bal_calc = True

# Collect User Data
data_format()
# Inputs
dollars = int(input("How many dollars do you have? "))
cents = int(input("How much change do you have? "))
# Collect User Input as strings
tot_dollars = str(dollars) + "." + str(cents)

# Print collected user_inputs
acct = Deposit(dollars, cents)

# Call box value for acct
sep_acct(acct)

# Build file to save data
write_text()

# Prompt to read file
read_file()

# Prompt for last balance
last_bal()

# Prompt for balance history
bal_history()
