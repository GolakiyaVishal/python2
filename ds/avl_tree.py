class AVLTree:
    def __init__(self):
        self.root = None

    # add new element in AVL tree
    def insert(self, val):
        print(f'insert: {val}')
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if not root:
            return self.Node(val)

        if val > root.val:
            root.right = self._insert(root.right, val)
        else:
            root.left = self._insert(root.left, val)
        
        root.height = max(self._getHeight(root.left), self._getHeight(root.right)) + 1

        root = self._balance(root)

        return root

    def _balance(self, root) :
        if self._isRightHeavy(root):
            if self._getBalanceFactor(root.right) > 0:
                root.right = self._rightRotation(root.right)
            root = self._leftRotation(root)
        elif self._isLeftHeavy(root):
            if self._getBalanceFactor(root.left) < 0:
                root.left = self._leftRotation(root.left)
            root = self._rightRotation(root)
        
        return root

    # Left Rotaion 
    def _leftRotation(self, node):
        print(f'LL: {node.val}')
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        
        node.height = self._calculateHeight(node)
        newRoot.height = self._calculateHeight(newRoot)

        return newRoot
    
    # Right Rotation
    def _rightRotation(self, node):
        print(f'RR: {node.val}')
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        
        node.height = self._calculateHeight(node)
        newRoot.height = self._calculateHeight(newRoot)

        return newRoot

    def _calculateHeight(self, node):
        return max(self._getHeight(node.left), self._getHeight(node.right)) + 1

    # get height of given node    
    def _getHeight(self, node):
        if not node:
            return -1
        return node.height

    def _isLeftHeavy(self, node) -> bool:
        return self._getBalanceFactor(node) > 1

    def _isRightHeavy(self, node) -> bool:
        return self._getBalanceFactor(node) < -1

    def _getBalanceFactor(self, node) -> int:
        return self._getHeight(node.left) - self._getHeight(node.right)

    # AVL Node
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.height = 0

if __name__ == '__main__':

    tree = AVLTree()
    tree.insert(12)
    tree.insert(3)
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(2)

    # tree = AVLTree()
    # tree.insert(5)
    # tree.insert(10)
    # tree.insert(3)
    # tree.insert(12)
    # tree.insert(15)
    # tree.insert(14)

    print('hello')

    # tree = AVLTree()
    # print('Left Rotation')
    # tree.insert(10)
    # tree.insert(20)
    # tree.insert(30)

    # tree = AVLTree()
    # print('Right Left Rotation')
    # tree.insert(10)
    # tree.insert(30)
    # tree.insert(20)

    # tree = AVLTree()
    # print('Right Rotation')
    # tree.insert(30)
    # tree.insert(20)
    # tree.insert(10)

    # tree = AVLTree()
    # print('Right Rotation')
    # tree.insert(30)
    # tree.insert(10)
    # tree.insert(20)


        