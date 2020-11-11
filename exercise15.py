#No hay control de errores, si se busca una persona que ya no está habrá un error y el programa petará
#entre otros errores
contact_list = []

def newContact(contact):
    contact_list.append(contact)

def searchContact(name):
    for i in contact_list:
        if i["Name"] == name:
            return i

def seeContacts():
    for i in contact_list:
        print("Contact full name: " + str(i["Name"]) + " " + str(i["Surname"]) + " " + str(i["Surname2"]) + " and number: " + str(i["Number"]))

def deleteContact(name):
    for i in contact_list:
        if i["Name"] == name:
            contact_list.remove(i)

def main():
    exit = False
    print("To exit just use any other value different than 1-4")
    while(not exit):
        options = int(input("What do you wanna do? (1: New contact, 2: Search contact, 3: See all contacts and 4: Delete contact)"))
        if options == 1:
            contact = {
                "Name": "",
                "Surname": "",
                "Surname2": "",
                "Number": 0,
            }
            name = input("Write the full name of the contact")
            name = name.split(" ")
            contact["Name"] = name[0]
            contact["Surname"] = name[1]
            contact["Surname2"] = name[2]
            contact["Number"] = int(input("Write the number of the contact"))
            newContact(contact)
        elif options == 2:
            name = input("Write the name of the contact")
            contact = searchContact(name)
            print("Contact full name: " + str(contact["Name"]) + " " + str(contact["Surname"]) + " " + str(contact["Surname2"]) + " and number: " + str(contact["Number"]))
        elif options == 3:
            seeContacts()
        elif options == 4:
            name = input("Write the name of the contact")
            deleteContact(name)
        else:
            exit = True

if __name__ == '__main__':
    main()