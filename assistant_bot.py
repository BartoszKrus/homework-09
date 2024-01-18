def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "User not found."
        except ValueError:
            return "The user already exists."
        except IndexError:
            return "Invalid format. Enter name and phone number."
    return inner


@input_error
def add_contact(phone_book, name, number):
    """
    The function adds the username and number to the phone book using the command:
    add <name> <number>
    """
    if name in phone_book:
        raise ValueError
    phone_book[name] = number
    return f"Contact {name} has been added."


@input_error
def update_contact(phone_book, name, number):
    """
    The function overwrites the existing user's number with the command:
    zmień <existing user> <new number>
    """
    if name not in phone_book:
        raise KeyError
    phone_book[name] = number
    return f"The phone number for {name} has been updated."


@input_error
def find_number(phone_book, name):
    """
    The function searches for a user's number by his name using the command:
    phone <user>
    """
    if name not in phone_book:
        raise KeyError
    return phone_book[name]


def show_all_contacts(phone_book):
    """
    The function displays the entire phone book using the command:
    show all
    """
    return "\n".join([f"{name}: {number}" for name, number in phone_book.items()])


def main():
    phone_book = {}

    while True:
        command = input("Enter command: ").lower()

        if '.' in command:
            break
        elif command in ['good bye', 'close', 'exit']:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add") and len(command.split(" ")) == 3:
            _, name, number = command.split(" ", 2)
            print(add_contact(phone_book, name.lower(), number))
        elif command.startswith("zmień") and len(command.split(" ")) == 3:
            _, name, number = command.split(" ", 2)
            print(update_contact(phone_book, name.lower(), number))
        elif command.startswith("phone") and len(command.split(" ")) == 2:
            _, name = command.split(" ", 1)
            print(find_number(phone_book, name.lower()))
        elif command == "show all":
            print(show_all_contacts(phone_book))
        else:
            print("Invalid command. Enter the correct command.")


if __name__ == "__main__":
    main()