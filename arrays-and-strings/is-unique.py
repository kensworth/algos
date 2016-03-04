#implement an algorithmto determine if a string has all unique characters
string1 = 'hello my name is ken'
string2 = 'abcdefghijklmnopqrstuvwxyz'

def isUnique(string):
	stringSet = set(string)
	print len(stringSet) == len(string)
isUnique(string1)
isUnique(string2)
