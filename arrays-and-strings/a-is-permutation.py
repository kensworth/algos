f=lambda a,b:0==cmp(*map(sorted,[a,b]))

'''
or
f=lambda a,b:sorted(a)==sorted(b)  #ResidentSleeper
'''

print f("anthony","nthonya") 
print f("anthony","anthonyzzzz") 
