def inverserPhrase(phrase):
    if phrase == None:
        return phrase
    i = 0
    phrase = phrase.split(' ')
    length = len(phrase) - 1
    while i <= length // 2:
        a = phrase[i]
        b = phrase[length - i]
        phrase[i] = b
        phrase[length - i] = a
        i+=1
    return phrase

print(inverserPhrase("bonjour tout le monde"))

