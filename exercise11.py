def capicua(phrase):
    ind = 0
    phrase = phrase.replace(" ","")
    word = phrase.lower()
    for reverse in reversed(word):
        if reverse == word[ind]:
            ind += 1
        else:
            return False
    return True

phrase = input("Write a phrase")
if capicua(phrase):
    print("The word: "+ phrase + " is capicua")
else:
    print("The word: "+ phrase + " is not capicua")