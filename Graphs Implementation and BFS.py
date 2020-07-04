# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:39:48 2020

@author: Kaushik
"""


class Graph:
    def __init__(self,nodes,is_directed=False):
        self.adj_list={}               #Create a Graph list which represents the dictionary wherin each node is a key and has a list of edges
        self.is_directed=is_directed
        for node in nodes:
            self.adj_list[node]=[]
    def add_nodes(self,nodes):
        for node in nodes:
            self.adj_list[node]=[]
    def print_adj_list(self):
        for node in self.adj_list:
            print(node,"->",self.adj_list[node])
    def add_edges(self,u,v):
        self.adj_list[u].append(v)
        if self.is_directed == False:
            self.adj_list[v].append(u)
    def bfs(self,source):
        queue=[] #Maintain a queue to explore the nodes
        level={} #used to store parents of the child nodes as well as used to check whether the node is already visited
        queue.append(source)
        level[source]=0
        #print(queue)
        #print(level)
        print("BFS-->")
        print(source)
        while len(queue)!=0: #while length of the queue not empty
            u=queue[0]       #extract the element and explore
            for v in self.adj_list[u]:
                if v not in level:
                    level[v]=level[u]+1
                    queue.append(v)
                    print(v)
            del queue[0] #delete after exploring
        print(level)
nodes=["A","B","C","D","E"]
g=Graph(nodes,is_directed=False)
edges=[("A","B"),("A","C"),("B","D"),("D","C"),("C","E"),("D","E")]
for u,v in edges:
    g.add_edges(u,v)
g.print_adj_list()
g.bfs("A")


#Takes O(|V|+|E|)
        
    