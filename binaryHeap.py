# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 13:06:20 2016

@author: LeBaron
"""

# binary heap (min-heap)

class BinHeap:
    def __init__(self):
        self.heapList = [0] # 0 to facilitate integer division
        self.currentSize = 0
        
        
        
    def bubbleUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i], self.heapList[i // 2] = self.heapList[i // 2], self.heapList[i]
            i = i // 2
            
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.ccurrentSize)
        
    def bubbleDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = self.heapList[mc], self.heapList[i]
            i = mc
            
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else: 
                return i * 2 + 1
                
    def removeMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.ccurrentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.bubbleDown(1)
        return retval
        
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.bubbleDown(i)
            i = i - 1

    def remove(self, name):
        index = [x[1] for x in self.heapList[1:]].index(name)
        self.heapList.pop(index + 1)
        self.buildHeap(self.heapList[1:])
        return self.heapList

       
    def changePriority(self, name, newPriority):
        index = [x[1] for x in self.heapList[1:]].index(name)
        self.heapList[index + 1], (newPriority, name) = (newPriority, name), self.heapList[index + 1]
        self.buildHeap(self.heapList[1:])
            
            
    
    
    
            
        
    