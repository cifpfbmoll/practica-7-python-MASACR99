
def wordJoiner(name,surname1,surname2):
    full_name = name + " " + surname1 + " " + surname2
    print(full_name)
    return full_name

name = input("Name")
surname1 = input("Surname")
surname2 = input("Second surname")
wordJoiner(name,surname1,surname2)