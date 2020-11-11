def spacesAreProhibited(phrase):
    return phrase.replace(" ", "")

phrase = input("Write something")
print(spacesAreProhibited(phrase))