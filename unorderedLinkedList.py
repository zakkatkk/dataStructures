# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:25:34 2016

@author: LeBaron
"""
from linkedList import Node

class UnorderedList:
    def __init__(self):
        self.head = None
        
    # evaluate whether the head is empty, thus the list is empty
    def isEmpty(self):
        return self.head == None
        
    # now we'll have to add a node to the list. It doesn't matter where I add the item
    # because it's unordered. If it were ordered we'd want to add it to the beginning
    # to spare traversing the list. 3 steps to add it:
        # 1. add node to list
            # define a new node 
            # set the next pointer of the new node
            # set the head to point at the new node
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        print(temp)
        
    def size(self):
        count = 0
        currentnode = self.head
        while currentnode != None:
            count += 1
            currentnode = currentnode.getNext()
        return count
        
        
mylist = UnorderedList()
mylist.add('1')
mylist.add('2')
mylist.add('3')
mylist.add('9')
print(mylist.size())


"""
notes from 10.5
    talking about the lab: if you want to pop the last element, size-1 is the last element of the list. 
    "draw it out and think about it carefully!"
    
    Suppose we have an unordered list we want to build a pop() for:
    (you cannot access nodes in the list by index b/c this isn't a built-in utility)
    List: head points to [10] points to [5] points to [2] points to ...
        consider 4 cases:
            CASE 1: 
                Pop the first index:            if position == 0:
                call a temporary variable:          temp = head
                change head pointer:                head.getNext()
                change size of the list:            size = size - 1
                return the value in the node:       return temp.getData()
                    
            CASE 2:
             First, we need the size of the list so we start at the beginning and move to the end.
             The position we want to pop is at the end of the list. position == size - 1
             We need two temps, one for the previous and one for the next.
             if pos == size - 1: 
                 prev = previous node 
                 tempData = pointer.getData()
                 p.setNext() = None
                 self.size -= 1
                 return current.getData()
                 
            CASE 3: the position we want to pop is somewhere in between the beginning and the end of the list.
            Need to keep two pointers, one that sits behind the current, so I can move the pointer of the current
            to that after the target.
            
            if pos >= position[0] & pos <= size - 1:
                p.setNext(current.getNext())
                self.size -= 1
                
            CASE 4: the list is empty. 
                if isEmpty(): return error message or whatever
                
        Talking about appending something to an unordered list:
            myList = List()
            mylist.add(70)
            mylist.append(30) mylist.append(10) ... all the way to the end
        
"""
        
"""
Double linked list...

# insert(25,5) insert(number,position)

# if the index is the first node...
if index == 0:
    n.setPrev(current.getPrev()) # sets previous pointer to the next one 
    current.setPrev(n)           # 
    n.setNext(current)           
    self.head = n                # repositioning the head of the list


# if the index is the last node... ????
elif index == size:
    n.setPrev = head.getPrev()
    self.head.setPrev(n)
    n.setNext = None
    prev = self.head
    current = prev.getNext()
    traverse list until we get to position
    prev.setNext = n
    
    




"""

























