class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
def build_tree(arr: list):
    stack = []
    root = TreeNode(arr[0])
    stack.append(root)
    i = 1
    l = len(arr)
    while i < l:
        parent = stack.pop(0)
        if i < l:
            parent.left = TreeNode(arr[i])
            stack.append(parent.left)
            i += 1
        if i < l:
            parent.right = TreeNode(arr[i])
            stack.append(parent.right)
            i += 1
    
    return root

def tree_prienter(root):
    if not root:
        return 
    
    tree_prienter(root.left)
    print(str(root.val) + " ")
    tree_prienter(root.right)

if __name__ == '__main__':
    tree_prienter(build_tree([1,2,3,4,5,6,7,8,9]))