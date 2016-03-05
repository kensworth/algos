#implement three stacks within a single array
#python 3 plz
#doesn't do error out of bounds checks (popping from empty) but that's easy

class stack3(object):
    def __init__(self):
        self.a = []
        self.end1=0
        self.end2=0
    def push1(self,value):
        self.a.insert(self.end1,value)
        self.end1+=1
        self.end2+=1
    def pop1(self):
        self.end1-=1
        self.end2-=1
        return self.a.pop(self.end1)
    def push2(self,value):
        self.a.insert(self.end2,value)
        self.end2+=1
    def pop2(self):
        self.end2-=1
        return self.a.pop(self.end2)
    def push3(self,value):
        self.a.append(value)
    def pop3(self):
        return self.a.pop()
    def p(self):
        print("actual array")
        print(self.a)
        print("segmented array")
        print(self.a[:self.end1], self.a[self.end1:self.end2], self.a[self.end2:])
        print()
s = stack3()
s.push1("A")
s.push1("B")
s.push1("C")
s.push1("D")
s.push2("E")
s.push2("F")
s.push3("G")
s.p()
print("popping from 2:",s.pop2())
s.p()
print("popping from 1:",s.pop1())
s.p()
print("pushing to 1: Z")
s.push1("Z")
s.p()
print("popping from 3:",s.pop3())
s.p()    
