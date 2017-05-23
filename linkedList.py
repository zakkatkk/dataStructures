# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:06:02 2016

@author: LeBaron
"""

"""
Linked lists
    ADT: Abstract Data Type: The type of behaviors that a data type should adhere to. 

    In a Python list the items themselves are not necessisarily ordered, but they do 
have a position relative position to other items in the list, index. 

    The key thing to know is that a linked list is the relationship between a pointer
and a node. The elements aren't necessisarily ordered, but it does have a beginning and
an end. 

    To access our list we have a pointer to the first element called a, "head". 
    pointer -> [head](pointer to next node) -> [data item](pointer to next node) -> ...
    
    This nature means we can insert items into the list without redefining the list in
memory. All we need to do is override the pointer in the preceeding node to point at
the new item. 

    To remove an element from a list, again the pointer in the preceeding node is 
simply redirected to another proceeding node. 

"""
# Examples:
# before i create a linked list I have to create a task 
class Node:
    def __init__(self,initdata):
        # everytime we create a node i have to send in the data
        self.data = initdata
        # since this function only creates the node then we don't need to make a pointer
        self.next = None
        
    def __str__(self):
        # convert the node into a string representation
        return str(self.data)
        
    # defining some getters and setters 
    def getData(self):
        return self.data
        
    def setData(self,newData):
        self.data = newData
        
    def getNext(self):
        return self.next
        
    def setNext(self,newPointer):
        self.next = newPointer
        
    
        
        
        














