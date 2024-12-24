# NOTE: Build terminal bank acct application using class, functions, and loops for practice
# from bank_data import data


# TODO: Create classes
class Deposit:
    def __init__(self, dol, cts):
        self.dollars = dol
        self.cents = cts

    def __str__(self):
        return "You deposited ${}.{:02} to your total balance.".format(
            self.dollars, self.cents
        )


# Function to create box around output
def sep_acct(val):
    print("=" * 45)
    print(val)
    print("=" * 45)


# Format data for file
def data_format():
    user_data["first_name"] = input("Enter your First Name: ").capitalize()
    user_data["last_name"] = input("Enter your Last Name: ").capitalize()
    user_data["age"] = int(input("Enter your age: "))


# Saves user input into a list
def save_input(user):
    user = []
    user.append(user)


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
sep_acct(acct)


# open user_data file
f = open("user_data.txt", "a")
# Write data_format Dictionary to file
f.write(f"{str(user_data)}\n")
# write inputs to File
f.write(f"Balance: ${tot_dollars}\n")

# Read file
# fr = open("user_data.txt", "r")
# print(fr.read)
