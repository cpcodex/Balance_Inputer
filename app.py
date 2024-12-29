import file_manager

file_name = file_manager.file_path
file_manager.save_user_data(file_name)
file_manager.read_user_data(file_name)
file_manager.search_user_data(file_name, search_key)

search_key = input("Which would you like to search for? ").strip().lower()
search_user_data(file_path, search_key)
print("=" * 50)


def main():
    # NOTE debugging NOTE
    # ============================================================================= #
    while True:
        fix = input(
            "Would you like to read, lookup, save, or quit this data? S, L, Q, or R "
        ).capitalize()

        if fix == "S":
            # Save user data
            save_user_data(file_path)
        elif fix == "R":
            # Read user data
            read_user_data(file_path)
        elif fix == "L":
            # search key in user data
            search_key = input("Which would you like to search for? ").strip().lower()
            search_user_data(file_path, search_key)
        elif fix == "Q":
            # Read user data
            print("Exiting input debugger...")
            break
        else:
            print("ERROR")


# Initiate the main file
if __name__ == "__main__":
    main()
