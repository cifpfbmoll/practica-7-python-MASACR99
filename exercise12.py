def wordCounter(phrase):
    counter = 0
    phrase = phrase.split()
    for i in phrase:
        counter += 1
    return counter

phrase = input("Write something")
print("There's " + str(wordCounter(phrase)) + " words in '" + str(phrase) + "'")