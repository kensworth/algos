#write a method to determine if one string is a permutation of another

str1 = 'hello'
str2 = 'leloh'
str3 = 'abcdefg'
str4 = 'qwerty'

def isPermutation(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False

print(isPermutation(str1, str2))
print(isPermutation(str3, str4))
