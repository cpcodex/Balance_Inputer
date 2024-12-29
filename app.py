import file_manager

# define file_manager for ease of use
file_name = file_manager.file_path
save = file_manager.save_user_data(file_name)
read = file_manager.read_user_data(file_name)
search = file_manager.search_user_data(file_name)
seperator = print("=" * 50)


def main():
    # Run while loop to begin program
    while True:
        fix = input(
            "Would you like to read, lookup, or save this data? R, L, or S.\n "
            "You may also input 'Q' to quit the program. "
        ).capitalize()

        if fix == "S":
            # Save user data
            save(file_name)
        elif fix == "R":
            # Read user data
            read(file_name)
        elif fix == "L":
            # search user data
            search(file_name)
        elif fix == "Q":
            # Quit program
            print("Exiting input debugger...")
            break
        else:
            print("INPUT ERROR!")


# Initiate the main file
if __name__ == "__main__":
    main()
