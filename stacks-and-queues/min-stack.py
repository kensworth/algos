# Design a stack which, in addition to push and pop, has a fucntion stackMin which returns the minumum element? Push, pop and min should all operate in O(1) time.

class stack(object):
    def __init__(self):
        self.arr = []
        self.stackMin = None
    def push(self, value):
        self.arr.append(value)
        if self.stackMin != None:
            if value < self.stackMin:
                self.stackMin = value
        else:
            self.stackMin = value
    def pop(self):
        return self.arr.pop(self)		
    def getMin(self):
        return self.stackMin
    def p(self):
        print(self.arr)

s = stack() 
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")
s.push("F")
s.push("G")
s.p()
print(s.getMin())
