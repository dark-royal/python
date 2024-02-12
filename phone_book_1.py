class Contacts:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        print(f"{name} ->{phone_number}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}'s -> {self.contacts[name]}")
        else:
            print(f"{name} not found in contact")

    def search_contact1(self, phone_number):
        if phone_number in self.contacts:
            print(f'{phone_number}-> {self.contacts[phone_number]}')
        else:
            print(f'{phone_number} not found in contact')

    def display_contacts(self):
        for name, phone_number in self.contacts.items():
            print(f"{name}->{phone_number}")


def main_menu():
    phonebook = Contacts()

    while True:
        print("""\nMain Menu:" +
        "\t\tEnter 1 -> Add phone_number" +
        "\t\tEnter 2 -> Search  for Contact with name" +
        "\t\tEnter 3 -> search for contact with phone_number" +
        "\t\tEnter 4-> Display Contacts" +
        "\t\tEnter 5-> Exit""")

        option = int(input("Enter your option (1-5 ): "))
        match option:
            case 1:
                name = input("Enter the contact_name: ")
                contact = input("Enter the phone number: ")
                phonebook.add_contact(name, contact)
            case 2:
                name = input("Enter the name to search: ")
                phonebook.search_contact(name)
            case 3:
                phone_number = input("Enter phone number")
                phonebook.search_contact1(phone_number)
            case 4:
                phonebook.display_contacts()
            case 5:
                print("Thanks Goodbye!")
                break
            case _:
                print("Invalid option")


main_menu()

# lists = [i for i in (range(5))]
# for i in range(10):
#     num = int(input("Enter number: "))
#     lists.append(num)
# print(lists)
