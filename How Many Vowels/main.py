

def countVowels(word):
    vowels = ['a','e','i','o','u']
    word_lower = word.lower()
    vowelsCounter = 0
    for letter in word_lower:
        if letter in vowels:
            vowelsCounter +=1
    return vowelsCounter


if __name__== "__main__":
    print(countVowels("ASD"))
    
