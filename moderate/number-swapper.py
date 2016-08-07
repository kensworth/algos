# write a function to swap a number in place in an array (no temp variables)

arr = [1, 2, 3, 4, 5]

def swap_in_place(arr, firstIndex, secondIndex):
    arr[firstIndex] = arr[firstIndex] ^ arr[secondIndex]
    arr[secondIndex] = arr[firstIndex] ^ arr[secondIndex]
    arr[firstIndex] = arr[firstIndex] ^ arr[secondIndex]
    print arr

print arr
swap_in_place(arr, 0, 4)


