
def changeTheWorld(phrase, vowel):
    vowels = ['a','e','i','o','u']
    changed_phrase = []
    for i in phrase:
        for j in i:
            if j.lower() in vowels:
                changed_phrase.append(vowel)
            else:
                changed_phrase.append(j)
    return ''.join(changed_phrase)

phrase = input("Write something")
vowel = input("What vowel do you want me to change to?")
print(changeTheWorld(phrase,vowel))