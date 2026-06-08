string = input("Bitte einen beliebigen Satz eingeben:  ")
wordlist = []
word = ""
for char in string:
    if not char == " ":
        word += char
    else:
        wordlist.append(word.lower())
        word = ""
wordlist.append(word.lower())

print(sorted(wordlist))
