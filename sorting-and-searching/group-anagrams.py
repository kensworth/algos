# Write a method to sort an array of strings so that all the anagrams are next to each other. 
test1 = [
    'abc', 'def', 'hij',
    'bca', 'efd', 'ijh',
    'cba', 'fed', 'jih'
]

def group_anagrams(arr):
    unique_set = set()
    unique_dictionary = {}
    new_arr = []
    for string in arr:
        sorted_string = ''.join(sorted(string))
        if sorted_string in unique_set:
           unique_dictionary[sorted_string].append(string) 
        else:
            unique_set.add(sorted_string)
            unique_dictionary[sorted_string] = [string]
    for unique_string in unique_dictionary:
        for anagram in unique_dictionary[unique_string]:
            new_arr.append(anagram)
    return new_arr

print group_anagrams(test1)
