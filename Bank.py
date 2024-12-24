# NOTE: reconsider how we store and access data.
# TODO: continue implementing data collection, access, and cleanup code
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


class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self):
        # Write file into txt file

        # open user_data file
        f = open(self.file_name, "a")
        # Write data_format Dictionary to file
        f.write(f"{str(user_data)}\n")
        # write inputs to File
        f.write(f"Balance: ${tot_dollars}\n")
        f.close()

    def read_file(self):
        # Prompts the user to read the file and displays its contents if the user agrees.
        read_file = input(
            'Do you wish to read the saved file? "Yes" or "No" '
        ).capitalize()

        if read_file == "Yes":
            # Read file
            fr = open(self.file_name, "r")
            print()
            print(fr.read())
        elif read_file == "No":
            print("No problem, the file was saved to your directory!")
        else:
            print("Error reading file")

    def find_file_param(self):
        # Finds paramater inside .txt file to compare to database.
        parameter = input('Do you wish to read the previous balance? "Yes" or "No" ')
        print("=" * 45)

        # Read file contents
        fr = open(self.file_name, "r")
        content = fr.read()

        # Check input with contents
        if parameter in content:
            print("Input is in database:", str(parameter))
        elif parameter not in content:
            print(str(parameter), "is not in the file.")
        else:
            print("Error is present")

    def last_bal(self):
        # Prompts the user to read the last balance from the file and displays it if the user agrees.
        bal_input = input(
            'Do you wish to read the previous balance? "Yes" or "No" '
        ).capitalize()

        if bal_input == "Yes":
            fr = open(self.file_name, "r")
            lines = fr.readlines()
            last_bal = lines[-1]
            print("=" * 45)
            print(last_bal)
        elif bal_input == "No":
            print("No problem, the file was saved to your directory!")
        else:
            print("Error reading file")

    def bal_history(self):
        # Prompts the user to view balance history and displays it if the user agrees.
        bal_hist = input(
            'Do you want to view your balance history? "Yes" or "No" '
        ).capitalize()
        print("=" * 45)

        if bal_hist == "Yes":
            fr = open(self.file_name, "r")
            lines = fr.readlines()
            for i in range(1, len(lines), 2):
                print(lines[i].rstrip("\n"))
            print()
        elif bal_hist == "No":
            print("No problem, the file was saved to your directory!")
        else:
            print("Error reading file")


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


# Print date
date()
# User Data Dictionary
user_data = {}
# Set app to true
bal_calc = True

# Collect User Data
data_format()
# Inputs
dollars = int(input("How many dollars are you depositing? "))
cents = int(input("How much change do you have to deposit? "))
# Collect User Input as strings
tot_dollars = str(dollars) + "." + str(cents)

# Print collected user_inputs
acct = Deposit(dollars, cents)

# Call box value for acct
sep_acct(acct)


if __name__ == "__main__":
    handler = FileHandler("user_data.txt")
    handler.write_file()
    handler.read_file()
    handler.last_bal()
    handler.bal_history()
    handler.find_file_param()
