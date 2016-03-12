#Given a directed graph, design an algorithm to find whether there is a route between two nodes. 
#This should be a cakewalk for you, A.
class KGraph(object):
    def __init__(self, V = [], E = []):
        self.V = V
        self.E = E
    def isRoute(self, node1, node2):
        for edge in self.E[node1]:
            if edge == node2 or self.isRoute(edge, node2): return True
        return False
        '''DFS'''
_V = [0,1,2,3,4,5,6,7,8,9,10,11,12]
_E = [[5,2,1,6],[],[],[],[3],[4,3],[4],[8],[],[10,11,12],[],[12],[]]
graph = KGraph(_V, _E)
print(graph.isRoute(0,5))
