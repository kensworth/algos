# You are given two sorted arrays, A and B, where A has a large enough buffer at the end to hold B. Write a method to merge B into A in sorted order.
a = [1,3,5,7,9]
b = [2,4,5,6,8,300]
c = 0;

while b:
 c+=a[c]<b[0]or bool(a.insert(c,b.pop(0)))
 if c==len(a):a,*b=a+b,

print(a)

#there's probably a more clever way to do this in 1 line
