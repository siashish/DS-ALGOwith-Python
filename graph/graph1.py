# graph = {1:set([2,3]),
#           2:set([4,3])}

class AdjNode:
    def __init__(self,value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self,num):
        self.V = num
        self.graph = [None]*self.V

    def add_edge(self,s,d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def print_agraph(self):
        for i in range(self.V):
            print("Vertex "+str(i)+" : ", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex),end="")
                temp = temp.next
            print(" \n")

if __name__=="__main__":
    V=5

    graph = Graph(V)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(0,2)
    graph.add_edge(2,3)
    graph.add_edge(3,4)
    print("First graph")
    graph.print_agraph()


    print("Second graph")
    graph1 = Graph(7)
    graph1.add_edge(0,1)
    graph1.add_edge(0,4)
    graph1.add_edge(4,2)
    graph1.add_edge(1,3)
    graph1.add_edge(2,5)
    graph1.add_edge(3,6)
    graph1.add_edge(5,6)
    graph1.add_edge(1,2)
    graph1.add_edge(3,5)

    graph1.print_agraph()