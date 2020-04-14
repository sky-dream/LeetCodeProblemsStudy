# -*- coding: utf-8 -*-  
# leetcode time     cost : 96 ms
# leetcode memory   cost : 13.8 MB
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Solution 1, 
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None: return l2
        if l2 == None: return l1

        def listnode2num(node):  # 将链表转换为数字(int)
            res = 0
            while node:
                res = res * 10 + node.val
                node = node.next
            return res

        result = listnode2num(l1) + listnode2num(l2)
        dummy_node = ListNode(0)  # 创建dummynode
        start_node = dummy_node
        for i in str(result):  # 讲结果相加结果转换为字符，然后逐位取出
            dummy_node.next = ListNode(int(i))  # 将取出的字符逐位放入新建的链表
            dummy_node = dummy_node.next
        return start_node.next