# NOTE: Note-bar is used to pick up where left off in previous session
# NOTE:
from datetime import date

today = date.today()


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


def data_format():
    # Format data for file
    user_data["first_name"] = input("Enter your First Name: ").capitalize()
    user_data["last_name"] = input("Enter your Last Name: ").capitalize()
    user_data["age"] = int(input("Enter your age: "))


def file_manager():
    # Write file into txt file

    # open user_data file
    f = open("user_data.txt", "a")
    # Write data_format Dictionary to file
    f.write(f"{str(user_data)}\n")
    # write inputs to File
    f.write(f"Balance: ${tot_dollars}\n")


def date():
    # Todays date
    formatted_date = today.strftime("%m/%d/%Y")
    print("Today is:", formatted_date)


date()
# User Data Dictionary
user_data = {}
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
file_manager()

# Read file
# fr = open("user_data.txt", "r")
# print(fr.read)
