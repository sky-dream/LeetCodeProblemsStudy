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
        if not head:
            return None
        if not head.next:
            return head            
        result = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return result
    
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