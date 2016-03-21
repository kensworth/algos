# You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.
a = [1,3,5,7,9]
b = [2,4,5,6,8]
a_counter = 0
b_counter = 0

for i in range(len(b)):
    if a[a_counter] <= b[b_counter] and a[a_counter + 1] > b[b_counter]:
        a.insert(a_counter + 1, b[b_counter])
        a_counter += 2
        b_counter += 1
    else:
        a_counter += 1

print(a)
