# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:46:09 2016

@author: LeBaron
"""

class HashTable:
        def __init__(self):
            self.size = 26
            self.data = [None] * self.size
            
        def put(self,data):
            hashvalue = self.hashfunction(data)
            print("hashvalue for ", data, " is: ", hashvalue)
            
            if self.data[hashvalue] == None:
                self.data[hashvalue] = data
            else:
                print("collision when placing:",data)
                nextslot = self.rehash(hashvalue,self.size)
                while self.data[nextslot] != None:
                    nextslot = self.rehash(nextslot.self.size)
                    
                self.data[nextslot] = data
                
        def hashfunction(self,str):
            char = str[0]
            return (ord(char) - 65)
            
        def rehash(self,str):
            #she had some print statements here
            (oldhash + 1) % size