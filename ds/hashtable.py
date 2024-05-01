from collections import deque

class HashTable:
    def __init__(self):
        self.table = [None] * 5

    
    def put(self, key, value):
        entry = self.Entry(key,value)

        index = self._getHash(key)
    
        if not self.table[index]:
            self.table[index] = deque[self.Entry]()
        
        
        for i, e in enumerate(self.table[index]):
            if key == e.key:
                e.value = value
                self.table[index][i] = e
                return
        
        self.table[index].append(entry)
        

    def get(self, key):
        index = self._getHash(key)

        ll = self.table[index]
        if ll:
            for e in ll:
                if e.key == key:
                    return e.value
        
        raise ValueError("No element found")
        
    def remove(self, key):
        index = self._getHash(key)

        if self.table[index]:
            for e in self.table[index]:
                if e.key == key:
                    self.table[index].remove(e)
                    return

        raise ValueError("No element found")

    def _getHash(self, key):
        return key % len(self.table)

    
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

if __name__ == '__main__':
    hashTable = HashTable()
    hashTable.put(3, "Sachin")
    hashTable.put(11, 'Parth')
    hashTable.put(11, 'Pintu')

    print(hashTable.get(3))
    print(hashTable.get(11))

    hashTable.remove(11)
    print(hashTable.get(11))


    