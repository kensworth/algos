def addM(M,N,i,j):
    print("N:\n"+formatBin(M,32)+"\nM:\n"+bin(N))
    a = formatBin(M,32)
    b = a[:-j] + formatBin(N,str(j-i)) + a[-i:]
    print(format("+",">"+str(33-j))+format("+","->"+str(j-i-1)),"\n"+b)

def formatBin(b,n):
    return format(bin(b).split("b")[1],"0>"+str(n))

addM(1,255,8,16)


'''
addM(1,255,8,16)

N:
00000000000000000000000000000001
M:
0b11111111
                +------+ 
00000000000000001111111100000001
'''
