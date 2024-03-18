"""
array is binary tree or not

input: ["(1,2)","(2,4)","(5,7)","(7,2)","(9,5)"]
output: True

input: ["(1,2)","(3,2)","(2,12)","(5,2)"]
output: False

input: ["(1,1)"]
output: False

["(2,5)", "(2,6)"]: false
["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)", "(1,9)"]: False
["(2,3)", "(1,2)", "(4,9)", "(9,3)", "(12,9)", "(6,4)"]: True
"""

def solution(strArr):
    tree = {}
    child = {}

    for e in strArr:
        leaf, node = e.replace("(", "").replace(")","").split(",")
        
        if leaf == node:
            return False
        
        t = tree.get(node, 0)

        if t >= 2:
            return False
        else:
            tree[node] = 1 + t

        k = child.get(leaf, 0)
        if k >= 1:
            return False
        else:
            child[leaf] = 1 + k

    return True


def is_valid_binary_tree(pairs):
    tree = {}
    roots = set()
    for e in pairs:
        child, parent = e.strip("()").split(",")
        if parent in tree:
            tree[parent].append(child)
        else:
            tree[parent] = child
            roots.add(parent)

    if len(roots) != 1:
        return False

    def is_valid(node):
        if node is not tree:
            return True
        children = tree[node]
        if len(children) > 2:
            return False
        elif len(children) == 1:
            return is_valid(children[0])
        elif len(children) == 2:
            return is_valid(children[0]) and is_valid(children[1])
    
    return is_valid(list(tree.keys())[0])


if __name__ == '__main__':
    print(is_valid_binary_tree(["(2,5)", "(2,6)"]))
