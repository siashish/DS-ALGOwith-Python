# Adjacency Matrix representation in python

class Graph(object):

    def __init__(self,size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self,v1,v2):
        if v1==v2:
            print("same vertex %d and %d"%(v1,v2))
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    
    def remove_edge(self,v1,v2):
        if self.adjMatrix[v1][v2]==0:
            print("No edge between %d and %d"%(v1,v2))
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1]=0
    
    def __len__(self):
        return self.size

    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)

def main():
    g = Graph(4)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(0,3)
    g.add_edge(1,2)
    g.add_edge(0,0)

    g.print_matrix()

    g.remove_edge(0,0)
    print()
    print(g.__len__())

    g.print_matrix()

    g1 = Graph(10)
    g1.add_edge(0,1)
    g1.add_edge(0,2)
    g1.add_edge(0,3)
    g1.add_edge(0,4)
    g1.add_edge(0,5)
    g1.add_edge(0,6)
    g1.add_edge(0,7)
    g1.add_edge(0,8)
    g1.add_edge(0,9)
    g1.add_edge(1,9)
    
    g1.print_matrix()

if __name__=='__main__':
    main()
