def capicua(word):
    ind = 0
    word = word.lower()
    for reverse in reversed(word):
        if reverse == word[ind]:
            ind += 1
        else:
            return False
    return True

word = input("Write a word")
if capicua(word):
    print("The word: "+ word + " is capicua")
else:
    print("The word: "+ word + " is not capicua")