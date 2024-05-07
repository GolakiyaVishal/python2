class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def height(node: Node):
    if not node:
        return -1
    
    return max(height(node.left), height(node.right)) + 1

def isPerfectBinaryTree(node: Node)->bool:

    # base case 
    if not node:
        return True
    
    # check for right and left both child exist or bot not exists
    if ((node.left and not node.right) or (not node.left and node.right)):
        return False

    # compare height of left and right sub tree
    if height(node.left) != height(node.right):
        return False
    
    # check for perfect left and right sub tree
    return isPerfectBinaryTree(node.left) and isPerfectBinaryTree(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(7)
root.right.right = Node(8)

root.left.left.left = Node(8)
root.left.left.right = Node(8)


if isPerfectBinaryTree(root):
    print("A perfect binary tree")
else:
    print("Not a perfect binary tree")
