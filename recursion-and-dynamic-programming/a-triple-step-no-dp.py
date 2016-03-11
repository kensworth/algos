c=lambda n:n if n<3 else 4if n==3 else c(n-1)+c(n-2)+c(n-3)
print(c(5))
print(c(14))
