from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.isEndOfWord = False

    def isContain(self, val):
        return val in self.children

    def insert(self, val):
        self.children[val] = Node(val)
    
    def getChildNode(self, val):
        return self.children[val]
    
    def removeChild(self, val):
        self.children.pop(val)

    def hasChildren(self):
        return len(self.children.items) >= 0

class Tries:
    def __init__(self):
        self.root = Node(" ")

    def insert(self, word):
        current = self.root
        for s in word:
            if not current.isContain(s):
                current.insert(s)
            current = current.getChildNode(s)
        current.isEndOfWord = True
    
    def isContain(self, word):
        current = self.root
        for s in word:
            if not current.isContain(s):
                return False
            current = current.getChildNode(s)
        return current.isEndOfWord
    
    def travers(self):
        self._traverse(self.root)

    def _traverse(self, node: Node):
        print(node.val)

        for key in node.children:
            self._traverse(node.children[key])
    
    def postOrderTraveral(self):
        self._postOrderTravers(self.root)

    def _postOrderTravers(self, node:Node):
        for key in node.children:
            self._postOrderTravers(node.children[key])
        print(node.val)
    
    def remove(self, word):
        if not word:
            return
        
        self._remove(self.root, word, 0)

    def _remove(self, node: Node,  word, index):
        if index == len(word):
            node.isEndOfWord = False
            return 
        
        val = word[index]
        if node.isContain(val):
            self._remove(node.getChildNode(val), word, index + 1)
        
        if node.getChildNode and not node.hasChildren:
            node.removeChild(val)

    def getAutoSuggestion(self, prefix):
        if not prefix:
            return

        list = []
        current = self.findLastNodeOf(prefix)
      
        list = self.__getSuggestion(current, list, prefix)

        return list
    
    def __getSuggestion(self, node:Node, list:List[str], word) -> List[str]: 
        if not node:
            return

        if node.isEndOfWord:
            list.append(word)

        for k in node.children.values():
            self.__getSuggestion(k, list, word + k.val)
        
        return list

    def findLastNodeOf(self, prefix) -> Node:
        current = self.root

        for s in prefix:
            if current.isContain(s):
                current = current.getChildNode(s)
        
        return current if current != self.root else None
    
    def countWords(self):
        count = 0
        return self.__countWords(self.root, count)
    
    def __countWords(self, node:Node, count) -> int:
        if node.isEndOfWord:
            count = count + 1

        for k in node.children.values():
            count = self.__countWords(k, count)
        
        return count

        

            

    

tries = Tries()
tries.insert("cat")
tries.insert("canada")

print(tries.countWords())

# print(tries.getAutoSuggestion("ca"))
# print(tries.isContain("cat"))
# tries.remove("cat")
# print(tries.isContain("cat"))
# tries.remove("can")
# print(tries.isContain("can"))

# print(tries.isContain("canada"))
# tries.travers()
# tries.postOrderTraveral()