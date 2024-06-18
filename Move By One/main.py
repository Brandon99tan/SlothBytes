def move(word):
    new_word =''
    for letter in word:
        new_word += chr(ord(letter)+1)
        #The ord() function returns the number representing the unicode code of a specified character.
        #chr() converts unicode back to character
    print(new_word)

if __name__ == '__main__':
    move("bye")