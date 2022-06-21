
import collections
import queue

def bfs(graph,root):
    visited,queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex)+" ",end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__=='__main__':
    graph = {0:[1,2,3],1:[0,2],2:[0,4],3:[0],4:[2]}
    print("print BFS")
    bfs(graph,4)

# time complexity O(V+E)
# space complexity O(V)