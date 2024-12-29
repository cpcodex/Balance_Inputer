import file_manager


# define file path for ease of use
file_name = file_manager.file_path


def main():
    # Run while loop to begin program
    while True:
        fix = input(
            "Would you like to read, lookup, or save this data? R, L, or S.\n"
            "You may also input 'Q' to quit the program.\n"
        ).capitalize()
        file_manager.data_seperator()

        if fix == "S":
            # Save user data
            file_manager.save_user_data(file_name)
            file_manager.data_seperator()
        elif fix == "R":
            # Read user data
            file_manager.read_user_data(file_name)
            file_manager.data_seperator()
        elif fix == "L":
            # search user data
            file_manager.search_user_data(file_name)
            file_manager.data_seperator()
        elif fix == "Q":
            # Quit program
            print("Exiting input debugger...")
            break
        else:
            print("INPUT ERROR!")


# Initiate the main file
if __name__ == "__main__":
    main()
