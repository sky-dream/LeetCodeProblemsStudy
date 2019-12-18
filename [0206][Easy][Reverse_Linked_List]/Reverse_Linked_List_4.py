# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.newHead = None
        def recursionHead(head):
            if not head:
                return head
            nextNode = recursionHead(head.next)
            head.next = None
            if nextNode:
                #for current node in current level,if next node is not none,reverse nextNode's pointer direction to current.  
                nextNode.next = head
            else:
                #for current node in current level,if next node is none,the taail is found,reverse it as the new head.
                self.newHead = head
            return head 
        recursionHead(head)
        return self.newHead
    
    def getLinkedListFromList(self,inputList):
        head = currentNode = ListNode(0)
        flag = 1
        for i in range(len(testList)):
            currentNode.val =  testList[i]
            if flag:
                head = currentNode 
                flag = 0
            currentNode.next = ListNode(0)
            if i == len(testList)-1:
                currentNode.next = None
            currentNode = currentNode.next
        return head
    
    def getListFromLinkedList(self,inputLinkedList):  
        result = []
        while inputLinkedList:
            result.append(inputLinkedList.val)
            inputLinkedList = inputLinkedList.next 
        return result
                                    
testList = [1,2,3,4,5,9,12,15]
s = Solution()
head = s.getLinkedListFromList(testList)
head = s.reverseList(head)
print(s.getListFromLinkedList(head))