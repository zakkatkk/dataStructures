
class HashTable:

    def __init__(self,size):
        self.size = size
        self.data = [None] * self.size
        self.overflow = []
        
    def putNoRehash(self,data):
        if isinstance(data,str) == True:
            hashvalue = self.H(data)
        else:
            hashvalue = self.remainderHash(data)
# if slot is empty, store data
        if self.data[hashvalue] == None:
            self.data[hashvalue] = data
        else: # no rehashing method so we'll just append overflow
            self.overflow.append(data)

# method not reusable outside of the specific cases of the assignment 
    def put(self,data):
        # handles the alpha and numeric cases
        if isinstance(data,str) == True:
            hashvalue = self.H(data)
        else:
            hashvalue = self.remainderHash(data)
        # alpha rehashing
        if isinstance(data,str) == True:
            if self.data[hashvalue] == None:
                self.data[hashvalue] = data
            else:
                hashvalue = self.H2(data)
                if self.data[hashvalue] == None:
                    self.data[hashvalue] = data
                else:
                    self.overflow.append(data)
#################### quadratic probing rehashing ############################
        else:
            if self.data[hashvalue] == None:
                self.data[hashvalue] = data
            else:
                offset = 1
                nextslot = self.rehash(hashvalue,offset)
######################## appends overloaded values into overflow list #######
                while offset <= self.size and self.data[nextslot] != None:
                    nextslot = self.rehash(nextslot,(offset**2))
                    offset += 1 
                if self.data[nextslot] == None:
                    self.data[nextslot] = data
                else:
                    self.overflow.append(data)

    def H(self,data):
        asciisum = 0
        data.lower()
        for character in data:
            charval = ord(character)
            asciisum += charval
        return charval % self.size
        
# multiplies the ASCII decimal value of each character by 10, sums them together, and mods by the table size.
    def H2(self,data):
        asciisum = 0
        data.lower()
        for character in data:
            charval = ord(character) * 10
            asciisum += charval
        return charval % self.size
        
# simple hash function
    def remainderHash(self,data):
        hashvalue = data % self.size
        return hashvalue
    
# quadratic probing collision resolution
    def rehash(self,oldhash,offset):
        from math import sqrt
        print("Attempt:", sqrt(offset), "Collision unresolved at position:", oldhash)
        print("Calculating new position:", oldhash + offset)
        return (oldhash + offset) % self.size
        

    
