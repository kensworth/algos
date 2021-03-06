#Given a directed graph, design an algorithm to find whether there is a route between two nodes. 
#This should be a cakewalk for you, A.

class Graph(object):
    def __init__(self,V=[],E=[]):
        self.V = V
        self.E = E
    def log(self):
        for i in range(len(self.V)):
            print(format(str(self.V[i])+":",'>3'),self.E[i])
    def routeBetween(self, start, end):
        print("starting at Vertex:",self.V[start])
        for edge in self.E[start]:
            if edge == end or self.routeBetween(edge, end):return True
        return False
            
_V = [0,1,2,3,4,5,6,7,8,9,10,11,12]
_E = [[5,2,1,6],[],[],[],[3],[4,3],[4],[8],[],[10,11,12],[],[12],[]]
g = Graph(_V, _E)

g.log()
print(g.routeBetween(0,3))




