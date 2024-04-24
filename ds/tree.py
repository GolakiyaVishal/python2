class Tree:
    def __init__(self):
        self.root = None

    
    def insert(self, val):
        node = self.Node(val)

        if not self.root:
            self.root = node
            return
        
        current = self.root
        while True:
            if val < current.val:
                if not current.leftNode:
                    current.leftNode = node
                    break
                current = current.leftNode
            else:
                if not current.rightNode:
                    current.rightNode = node
                    break
                current = current.rightNode

    def find(self, val):
        current = self.root
        while current:
            if val < current.val:
                current = current.leftNode
            elif val > current.val:
                current = current.rightNode
            else:
                return True
        return False

    class Node:
        def __init__(self, val):
            self.val = val
            self.leftNode = None
            self.rightNode = None

if __name__ == '__main__':
    tree = Tree()
    tree.insert(7)
    tree.insert(2)
    tree.insert(8)
    tree.insert(9)

    print(tree.find(8))
    print(tree.find(10))