# -*- coding: utf-8 -*-  
# leetcode time     cost : 92 ms
# leetcode memory   cost : 13.7 MB
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Solution 1, 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getNum(listNode: ListNode):
            res = 0
            while listNode:
                res = res*10 + listNode.val
                listNode = listNode.next
            return res
        def genList(num):
            numList = []
            # do spacial handle if num == 0 when l1=[0],l2=[0]
            if num == 0: return ListNode(0)
            while num:
                numList.append(num % 10)
                num = num // 10
            numList = numList[::-1]
            dummyNode = ListNode(-1)
            current = ListNode(numList[0])
            dummyNode.next = current
            for i in range(1,len(numList)):
                current.next = ListNode(numList[i])
                current =  current.next
            return dummyNode.next
        sumNum = getNum(l1) + getNum(l2)
        #print("sumNum:",sumNum,",getNum(l1):",getNum(l1) ,",getNum(l2):", getNum(l2))
        return genList(sumNum)