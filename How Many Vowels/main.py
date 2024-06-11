

def countVowels(word):
    vowels = ['a','e','i','o','u']
    vowelsCounter = 0
    for letter in word:
        if letter in vowels:
            vowelsCounter +=1
    return vowelsCounter


if __name__== "__main__":
    word = input("Enter your word: ")
    print(f"The number of vowels in the word '{word}' is: {countVowels(word.lower())}")
    
    