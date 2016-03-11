countSteps=lambda n:n if n<3 else 4if n==3 else sum(map(countSteps,range(n-3,n)))

print(countSteps(5))
print(countSteps(14))
