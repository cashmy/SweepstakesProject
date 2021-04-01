import os


def simulation_main_menu():
    """Main menu prompting user to choose an option"""
    validate_user_selection = (False, None)
    while validate_user_selection[0] is False:
        print("\n\t\t-Sweepstake Processing-")
        print("\tPress -1- to create a sweepstakes")
        print("\tPress -2- to create and assign a contestant")
        print("\tPress -3- to generate a sweepstakes winner")
        print("\tPress -4- to remove a sweepstakes")
        print("\tPress -5- to exit")
        user_input = try_parse_int(input())
        validate_user_selection = validate_main_menu(user_input)
        if validate_user_selection[0] is False:
            print("Not a valid selection try again")
    return validate_user_selection[1]


def validate_main_menu(user_input):
    """Validation function that checks if 'user_input' argument is an int 1-4. No errors."""
    switcher = {
        1: (True, 1),
        2: (True, 2),
        3: (True, 3),
        4: (True, 4),
        5: (True, 5),
    }
    return switcher.get(user_input, (False, None))


def display_welcome():
    """Initial method asking user if they'll make a purchase. No errors."""
    print("\nWelcome to the Sweepstakes backend management. \n")
    user_response = bool_prompt("Would you like to work on your sweepstakes database? (y/n): ")
    if user_response:
        return True
    else:
        print("Please sign off and conserve your precious technological resources.")
        return False


def output_text(text):
    """User input method that will print to console any string passed in as an argument"""
    print(text)


def clear_console():
    """Used for clearing out the console. No errors."""
    os.system('cls' if os.name == 'nt' else "clear")


def bool_prompt(text):
    """Validates a 'y' or 'yes' string and returns a True value. No errors."""
    switcher = {
        "y": True,
        "yes": True
    }
    user_input = input(text).lower()
    return switcher.get(user_input, False)


def try_parse_int(value):
    """Attempts to parse a string into an integer, returns 0 if unable to parse. No errors."""
    try:
        return int(value)
    except:
        return 0


def contest_info_print():
    # TODO: print out information here
    pass


def sweeps_type_menu():
    validate_user_selection = (False, None)
    while validate_user_selection[0] is False:
        print("\n\t\t-Sweepstakes MANAGER Type-")
        print("\tPress -1- to create a sweepstakes Stack")
        print("\tPress -2- to create a sweepstakes Queue")
        print("\tPress -3- to exit")
        user_input = try_parse_int(input())
        validate_user_selection = validate_sweeps_type_menu(user_input)
        if validate_user_selection[0] is False:
            print("Not a valid selection try again")
    return validate_user_selection[1]


def validate_sweeps_type_menu(user_input):
    """Validation function that checks if 'user_input' argument is an int 1-3. No errors."""
    switcher = {
        1: (True, 1),
        2: (True, 2),
        3: (True, 3),
    }
    return switcher.get(user_input, (False, None))


def enter_sweepstake_name():
    return input('Please enter the name of this sweepstake: ')


def get_contestant_info():
    first_name = input("Enter contestant's first name: ")
    last_name = input("Enter contestant's last name: ")
    email = input("Enter contestant's email: ")
    return first_name, last_name, email
