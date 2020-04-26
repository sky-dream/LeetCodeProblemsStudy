# leetcode time     cost : 156 ms
# leetcode memory   cost : 17.8 MB 
# Time  Complexity: O(Nlogk),
# Space Complexity: O(N)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# solution2. min heap
from typing import List
class Solution:
    def mergeKLists(self, lists: List[ListNode]):
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                # notes, at start,node pointer already mover to 2nd node of link list,
                # val: 1 ,idx, 0 ,lists[idx].val, 4
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next        
        return dummy.next
    def buildLinkList(self, inputList):
        dummy = ListNode(0)
        p = dummy   
        for val in  inputList:
            p.next = ListNode(val)
            p = p.next
        return dummy.next
    def outputLinkList(self, linkList):
        res = []
        while linkList:
            res.append(linkList.val)
            linkList = linkList.next
        return res
    def preProcess(self, linkedNode_List):
        convertedInputX = []
        for listinput in linkedNode_List:
            tmplinklist = self.buildLinkList(listinput)
            convertedInputX.append(tmplinklist)
        return convertedInputX
    
def main():
    inputX,expectRes = [[1,4,5],[1,3,4],[2,6]] ,[1,1,2,3,4,4,5,6]
    obj = Solution()
    convertedInputX = obj.preProcess(inputX)
    result = obj.mergeKLists(convertedInputX)
    try:
        assert obj.outputLinkList(result) == expectRes
        print("passed, result is follow expect:",result)
    except AssertionError as aError:
        print('failed, result >> ', outputLinkList(result),"<< is wrong, ","expect is : ", expectRes)
    
if __name__ =='__main__':
    main() 