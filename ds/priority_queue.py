class PriorityQueue:
    def __init__(self):
        self.queue = [None] * 5
        self.count = 0

    def insert(self, val):
        if self.count == 5:
            raise ValueError("Index out of bound")
        
        i = self.count - 1
        for i in range(self.count-1, -1, -1):
            if self.queue[i] > val:
                self.queue[i + 1] = self.queue[i]
            else:
                break
        self.queue[i+1] = val
        self.count += 1
        
    def remove(self):
        if self.count == 0:
            raise ValueError("No element")
        
        tmp = self.queue[self.count-1]
        self.queue[self.count-1] = None
        self.count -= 1
        return tmp

    def printQueue(self):
        print(self.queue)
    
if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert(1)
    pq.insert(5)
    pq.insert(4)
    pq.insert(3)
    pq.insert(2)
    pq.printQueue()
    print(pq.remove())
    pq.printQueue()
    print(pq.remove())
    pq.printQueue()
    print(pq.remove())
    pq.printQueue()
    print(pq.remove())
    pq.printQueue()
    print(pq.remove())
    pq.printQueue()
    print(pq.remove())
    pq.printQueue()
