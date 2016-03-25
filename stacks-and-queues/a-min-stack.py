class stack(object):
    def __init__(self):
        self.arr = []
        self.stackMin = None
    def push(self, value):
        self.arr.append(value)
        if self.stackMin == None:
            self.stackMin = value
        else:
            self.stackMin = min(self.stackMin,value)
    def pop(self):
        return self.arr.pop()		
    def getMin(self):
        return self.stackMin
    def p(self):
        print(self.arr)

s = stack() 
s.push(3)
s.push(4)
s.push(5)
s.push(1)
s.push(2)
s.push(4)

s.p()
print(s.getMin())
