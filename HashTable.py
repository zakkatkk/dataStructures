# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:03:11 2016

@author: LeBaron
"""

# uses 2 lists to create a Hash Table class that implements the Map ADT. One list, called slots, will hold the key items and a parallel list, called data, will hold the values.
# implements a simple remainder hash function with linear probing rehash

class HashTable:
    
    def __init__(self):
        self.size = 11 # arbitrary but should be a prime number
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self, key, data):
        hasvalue = self.hashfunction(key,len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data # replace
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data # replace
                    
    def hashfunction(self,key,size):
        return key % size
        
    def rehash(self, oldhash, size):
        return (oldhash + 1) % size
        
    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data
    
    def __getitem__(self, key):
        return self.get(key)
        
    def __setitem__(self, key, data):
        self.put(key, data)
        
                    
            
                
                
                
                
                
                
                
                
                