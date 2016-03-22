h = {0:1,1:1,2:2}
def c(n):
    if n in h: return h[n]
    j = c(n-1) + c(n-2) + c(n-3)
    h[n] = j
    return j

print(c(10))
print(c(5))
