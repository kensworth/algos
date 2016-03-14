#You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to insert M in  N such that M starts at bit j and ends at bit i. You can assume that the bits j through i have enough space to fit all of M. That is, if M = 10011, you can assume there are at least 5 bits between j and i. You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
M = 88 
N = 12131213121377
print('M: ', bin(M))
print('N: ', bin(N))
'''
('M: ', '0b1011000')
('N: ', '0b1001000100110110011100100010111')
'''
i = 12
j = 3

M = M << (i - j)
N = N | M
print('N: ',bin(N))




