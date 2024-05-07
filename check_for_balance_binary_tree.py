# Check if the given binary tree is balanced or not

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class Solution:
    def __height(self, node: Node):
        if not node:
            return -1
        
        return max(self.__height(node.left), self.__height(node.right)) + 1

    def isBalanced(self, node: Node):
        
        # base case
        if not node:
            return True
        
        
        left = self.__height(node.left)
        right = self.__height(node.right)

        # check for height factor
        # 1 and -1 difference
        if (abs(left-right) <= 1  and 
            self.isBalanced(node.left) and
            self.isBalanced(node.right)):
            return True

        # default case
        return False
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)
if Solution().isBalanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")