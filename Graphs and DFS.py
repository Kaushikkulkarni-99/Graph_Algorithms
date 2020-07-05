# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:38:21 2020

@author: Kaushik
"""

parent={}       #Global Parent For DFS
class Graph:
    def __init__(self,nodes,is_directed=False):
        self.adj_list={}
        self.is_directed=is_directed
        for node in nodes:
            self.adj_list[node]=[]
        
    def add_edges(self,edges):
        for u,v in edges:
            self.adj_list[u].append(v)
            if self.is_directed==False:
                self.adj_list[v].append(u)
        print(self.adj_list)
    
    def bfs(self,source):
        queue=[]
        level={}
        parent={}
        queue.append(source)
        level[source]=0
        parent[source]=None
        print("BFS-->")
        print(source)
        while len(queue) != 0:
            u=queue[0]
            del queue[0]
            for v in self.adj_list[u]:
                if v not in level:    #search for the key in level {A:0,B:1,C:1 ....}
                    level[v]=level[u]+1
                    parent[v]=u
                    queue.append(v)
                    print(v)
        print("Parents are:",parent)
        print("levels are:",level)
        
    def dfs(self,source):                       #DFS starts here
        global parent                           #we need to call recursively all the nodes connected to source
        print(source)                           #recursively and explore those nodes
        for v in self.adj_list[source]:         #for each next call source is the node connected to its parent
            if v not in parent:                 #ahere we use stack implicitely in the form of function
                parent[v]=source
                self.dfs(v)
        print(parent)
            
#main BLOCK        
nodes=["A","B","C","D","E"]
edges=[("A","B"),("A","C"),("B","D"),("D","C"),("C","E"),("D","E")]
g=Graph(nodes,is_directed=False)
g.add_edges(edges)
g.bfs("A")
parent["A"]=None
g.dfs("A")

#Takes O(|V|+|E|) time
