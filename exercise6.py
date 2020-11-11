def finder(name,letter):
    if letter in name:
        return True
    else:
        return False

name = input("Whats ur name?")
letter = input("Letter to find?")
print(finder(name,letter))