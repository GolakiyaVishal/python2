# https://leetcode.com/problems/add-two-numbers/description/

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def addTwoList(self, l1, l2):
        str1 = self.getAsString(l1)[::-1]
        str2 = self.getAsString(l2)[::-1]
        sm = int(str1) + int(str2)
        sm = (str(sm))[::-1]

        head = ListNode(sm[0])
        current = head
        for i in range(1, len(sm)):
            current.next = ListNode(int(sm[i])) # m1
            current = current.next # m2
        
        return head # m3

    
    def getAsString(self, l1):
        resp = ""
        head = l1
        while (head != None):
            resp += str(head.val) #m4
            head = head.next
        return resp

def getHead(arr1):
    head = ListNode(arr1[0])
    current = head
    for e in arr1[1:]:
        current.next = ListNode(e)
        current = current.next
    return head

if __name__ == '__main__':
    Solution().addTwoList(getHead([2,4,3]), getHead([5,6,4]))
