# def createAdjList(edges):
#     adjList = {}
#     for edge in edges:
#         node1, node2 = edge
#         if node1 not in adjList:
#             adjList[node1] = []
#         if node2 not in adjList:
#             adjList[node2] = []
#         adjList[node1].append(node2)
#         adjList[node2].append(node1)
#     return adjList

from collections import defaultdict

def createAdjList2():
    n= int(input("Enter the number of nodes: "))
    adj_list= defaultdict(list)
    for i in range(n):
        node=input ("Enter node: ")
        adj_list[node]=[]
    edges= int(input(f"Enter the number of edges for node {node}: "))
    for i in range(edges):
        s=input("Enter your source node ")
        d=input("Enter your destination node ")
        adj_list[s].append(d)
        adj_list[d].append(s)
    return adj_list

myAdjList = createAdjList2()
print(myAdjList)