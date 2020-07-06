# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:50:24 2020

@author: Kaushik
"""


class Heap:
    def __init__(self):
        self.heap=[0]
        
    def _heapify(self,ele):
        i=self.i
        while i>1:
            if(self.heap[i//2]<self.heap[i]):
                self.heap[i//2],self.heap[i]=self.heap[i],self.heap[i//2]
                i=i//2
            else:
                break                
    def _rearrange(self):
        l=len(self.heap)-1
        i=1
        while(i<=l/2):
            largest=i
            left=2*i
            right=2*i+1
            if(left<l and self.heap[left]>self.heap[largest]):
                largest=left
            if(right<l and self.heap[right]>self.heap[largest]):
                largest=right
            if largest != i:
                self.heap[i],self.heap[largest]=self.heap[largest],self.heap[i]
                i=largest
            else:
                break
        print("After Popping Final Heap:",self.heap)
    
    def push(self,ele):
        self.heap.append(ele)
        self.i=len(self.heap)-1
        print(self.i)
        self._heapify(ele)
        print("After pushing Heap Final:",self.heap)
        
    def pop(self):
        self.i=len(self.heap)-1
        self.heap[self.i],self.heap[1]=self.heap[1],self.heap[self.i]
        self.heap.pop()
        self._rearrange()
        
        
#Main function starts here
h=Heap()
h.push(10)
h.push(20)
h.push(8)
h.push(30)
h.push(25)
h.push(5)
h.push(3)
h.pop()
