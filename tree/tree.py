# Parent Node
# Child Node
# Root Node
# Degree of a Node
# Leaf Node/ external Node
# Inernal Node
# Depth of the node
# Height of Node
# Sibling
# Ancestor of a Node
# Desecendent 
# Level of a Node
# Subtree

# def printPraents(node,adj,parent):
#     if(parent==0):
#         print(node,"->Root")
#     else:
#         print(node,"->",parent)

#     for

N =7
Root=1

#Adjestent list
adj = []
for i in range(0,N+1):
    adj.append([])

print(adj)

# tree
adj[1].append(2)
adj[1].append(3)
adj[1].append(4)

adj[2].append(1)
adj[2].append(5)
adj[2].append(6)

adj[3].append(1)

adj[4].append(1)
adj[4].append(7)

adj[5].append(2)

adj[6].append(2)

adj[7].append(4)

print(adj)


