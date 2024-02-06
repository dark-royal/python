

def display():
        print("WELCOME TO PHONEBOOK")
def display1():
    print("Main menu \n" +
     "\t\t\tEnter 1 -> Collect contact and store: \n" +
     "\t\t\tEnter 2 -> Search for contact:  \n" +
     "\t\t\tEnter 0 -> Exit:  ")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    option = int(input("Enter option: "))
    match option:
        case 1:
            collectContact()
        case 2:
            searchForContacts()
        case 0:
             exit()

        case _:
             print("Enter a valid option: ")
def collectContact():
    phone_number = input("Add phone number: ")

    full_name = input("Enter full name: ")
    # put(phone_number, full_name)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Saved Successfully")
    display1()



def collectAddress():
        address = input("Enter the address")
        print("LOADING.......SAVED SUCCESSFULLY")
def searchForContacts():
        name = input("Enter name to search")
        print((name, "No information found relating to the name"))
print(display1())
