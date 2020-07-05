# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:03:34 2020

@author: Kaushik
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:12:12 2020

@author: Kaushik
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 09:38:21 2020

@author: Kaushik
"""

import sys

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
        
    def dfs_visit(self):
        global parent
        for s in self.adj_list:
            if s not in parent:
                parent[s]=None
                self.dfs(s)
                
                
    def cycle_detect_undirected(self,source):   #WORKS FOR DIRECTED ALSO
        global parent                           
        global stack
        stack[source]=source 
        for v in self.adj_list[source]:
            if v in stack and parent[source]!=v:
                print("Cycle:",source,v,"Visited:")
                sys.exit("Cycle Found")
                
            if v not in parent:                 
                parent[v]=source
                self.cycle_detect_undirected(v)
        del stack[source]
    
    
    def cycle_for_undirected(self):
        global parent
        for s in self.adj_list:
            if s not in parent:
                parent[s]=None
                self.cycle_detect_undirected(s)
        
        
#main BLOCK        
nodes=["A","B","C","D","E","M","Z"]
edges=[("A","B"),("A","C"),("B","D"),("C","D"),("D","E"),("B","E"),("D","A")]
g=Graph(nodes,is_directed=True) #Here the graph is directed
g.add_edges(edges)
g.dfs_visit() 
print("Whether The graph contains cycle")
parent={}    #Again initialised parent to empty because we have accesed g.dfs_visit() in order to have better understanding about how graph was travered
stack={}
visited_times={}
g.cycle_for_undirected()
print(visited_times)
print("Cycle Not Found")
 

#Takes O(|V|+|E|) time
