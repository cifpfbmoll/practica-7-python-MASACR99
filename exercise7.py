def vowelCounter(phrase):
    counter = [0,0,0,0,0]
    phrase = phrase.lower()
    counter[0] = phrase.count('a')
    counter[1] = phrase.count('e')
    counter[2] = phrase.count('i')
    counter[3] = phrase.count('o')
    counter[4] = phrase.count('u')
    return counter

phrase = input("Write something")
numbers = vowelCounter(phrase)
print("There's "+ str(numbers[0]) + " a, "+str(numbers[1]) +" e, "+str(numbers[2]) +" i, "+str(numbers[3]) +" o, "+str(numbers[4]) +" u.")