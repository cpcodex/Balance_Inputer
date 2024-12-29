import file_manager


def data_seperator():
    # Seperator
    return "=" * 40


# define file path for ease of use
file_name = file_manager.file_path


def start():
    print(
        " Welcome to the Terminal Bank Account.\n",
        data_seperator(),
        "\n You can input 'R' to Read, 'L' to Lookup, or 'S' to Save from the data file.\n"
        " You may also input 'Q' to quit the program.\n",
    )


start()


def main():
    # Run
    while True:
        # while loop to begin program

        # input used to access program
        fix = input("Would you like to read, lookup, or save the data?\n").capitalize()

        if fix == "S":
            # Save user data
            file_manager.save_user_data(file_name)
            data_seperator()
        elif fix == "R":
            # Read user data
            file_manager.read_user_data(file_name)
            data_seperator()
        elif fix == "L":
            # search user data
            file_manager.search_user_data(file_name)
            data_seperator()
        elif fix == "Q":
            # Quit program
            print("Exiting input debugger...")
            break
        else:
            print("INPUT ERROR!")


# Initiate the main file
if __name__ == "__main__":
    main()
