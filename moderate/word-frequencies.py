# Design a method to find the frequency of occurrrences of any given word in a book. What if we were running this algorith multiple times?
import string 

passage = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
out = passage.translate(string.maketrans("",""), string.punctuation)
wordList = out.split()

dictionary = {}
for word in wordList:
    if word in dictionary: 
        dictionary[word] += 1
    else:
        dictionary[word] = 1

print dictionary
