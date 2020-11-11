
def charPerLine(phrase):
    for i in phrase:
        for j in i:
            print(j)

phrase = input("Write something")
charPerLine(phrase)