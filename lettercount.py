#6.3
#function that takes a word and a letter as inputs
#check to make sure inputs are strings
#for loop that matches input letter to letters in the word
#print # of times the letter appears

def count (word, letter):
    word = str(word)
    letter = str(letter)
    count = 0
    for ls in word:
        if ls == letter : count += 1
    print (count)