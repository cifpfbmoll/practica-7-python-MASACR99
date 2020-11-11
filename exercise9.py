def rimeMonster(word1,word2):
    if word1[-3:] == word2[-3:]:
        return "They rime~"
    elif word1[-2:] == word2[-2:]:
        return "They kinda rime"
    else:
        return "They don't rime"

word1 = input("Write soemthing")
word2 = input("Write soemthing else")
print(rimeMonster(word1,word2))