c=lambda n:eval(("1","n","c(n-3)+c(n-2)+c(n-1)")[bool(n)+(n>2)])

print(c(10))
print(c(5))
