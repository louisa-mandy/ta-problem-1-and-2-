'''
Problem 1:
Mr David is playing a word-linking game. In this game, a word is considered to be linked to the previous word if at least one letter at the beginning of the word matches the last letter of the previous word. Create a program that can take two words as input and determine whether these two words can be used in the word-linking game. If they can, the program should also display the longest subword that can link the two given words.

Example 1:

Length of the first word: 8

First word: accuracy

Length of the second word: 8

Second word: cylinder

Both words can be linked with the subword 'cy'.

Example 2:

Length of the first word: 7

First word: physics

Length of the second word: 9

Second word: chemistry

Both words cannot be linked.
'''
def find_linking_subword(word1, word2):
    len_word1 = len(word1)
    len_word2 = len(word2)

    # Find the minimum length to iterate over
    min_len = min(len_word1, len_word2)

    # Iterate from the beginning to find the longest subword
    linking_subword = ''
    for i in range(1, min_len + 1):
        if word1[-i:] == word2[:i]:
            linking_subword = word1[-i:]
    
    return linking_subword

def word_linking_game():
    # Input the first word
    word1 = input("First word: ")
    print("First word :", word1)
    length_word1 = len(word1)
    print("Length of first word:", length_word1)

    # Input the second word
    word2 = input("Second word: ")
    print("Second word :", word2)
    length_word2 = len(word2)
    print("Length of second word:", length_word2)

    # Check if the words can be linked
    linking_subword = find_linking_subword(word1, word2)

    if linking_subword:
        print(f"Both words can be linked with the subword '{linking_subword}'.")
    else:
        print("Both words cannot be linked.")

# Run the word linking game
word_linking_game()

'''
word1_length = "word length = 8"
word1 = input(" enter first word: ")
print(word1_length)
input()
print(word1)

input()
word2_length = "word length = 8"
word2 = input("enter second word: ")

print(word2_length)
input()
print(word2)

word_linking_game(word1, word2)
'''