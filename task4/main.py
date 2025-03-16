# Parse user input.
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Add new contact.
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
    else:
        return "Invalid input. Proper format to use: 'add' 'name' 'phone'."
    if name in contacts:
        return "Contact already exist, please enter different name."
    else:
        contacts[name] = phone
        return "Contact added."

# Change existing contact.
def change_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
    else:
        return "Invalid input. Proper format to use: 'change' 'name' 'phone'."
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else: "Contact not found."

# Show phone for requested user.
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
    else:
        return "Invalid input. Proper format to use: 'phone' 'name'."
    if name in contacts:
        return contacts[name]
    else: "Contact not found."

# Show all contacts.
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()