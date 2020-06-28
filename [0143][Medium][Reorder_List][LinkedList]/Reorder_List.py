# -*- coding: utf-8 -*- 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
# leetcode time     cost : 116 ms
# leetcode memory   cost : 23.1 MB
# solution 1, using stack
# Time  Complexity: O(N)
# Space Complexity: O(N)
# https://leetcode-cn.com/problems/reorder-list/solution/yong-zhan-fan-zhuan-huo-zhe-zhi-jie-fan-zhuan-by-p/
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head: return None
        p = head
        stack = []
        # 把所有节点压入栈中
        while p:
            stack.append(p)
            p = p.next
        # 长度
        n = len(stack)
        # 找到中点前一个位置 
        count = (n - 1) // 2
        p = head
        while count:
            # 弹出栈顶
            tmp = stack.pop()
            # 与链头拼接
            tmp.next = p.next
            p.next  = tmp
            # 移动一个位置
            p = tmp.next
            count -= 1
        stack.pop().next = None   