def characters():
    while True:
        word = input('Enter a word: ')
        if len(word) < 5:
            print("Your word is less than 5 characters")
        elif len(word) > 5:
            print("Your word is more than 5 characters")
        else:
            print("Your word is equal to 5 characters")
    if not word:
        return word

print (characters())



