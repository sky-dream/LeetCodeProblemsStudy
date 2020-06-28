# -*- coding: utf-8 -*- 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
# leetcode time     cost : 108 ms
# leetcode memory   cost : 23.2 MB
# solution 2, reverse linked list
# Time  Complexity: O(N)
# Space Complexity: O(N)
# https://leetcode-cn.com/problems/reorder-list/solution/yong-zhan-fan-zhuan-huo-zhe-zhi-jie-fan-zhuan-by-p/
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        # 1 2 3 4 5
        fast = head
        pre_mid = head
        # 找到中点, 偶数个找到中点前面那个
        while fast.next and fast.next.next:
            pre_mid = pre_mid.next
            fast = fast.next.next
        # 翻转中点之后的链表,采用是pre, cur双指针方法
        pre = None
        cur = pre_mid.next
        # 1 2 5 4 3
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 翻转链表和前面链表拼接
        pre_mid.next = pre
        # 1 5 2 4 3
        # 链表头
        p1 = head
        # 翻转头
        p2 = pre_mid.next
        #print(p1.val, p2.val)
        while p1 != pre_mid:
            # 前后节点拼接
            pre_mid.next = p2.next
            p2.next = p1.next
            p1.next = p2
            # 节点向前推进
            p1 = p2.next
            p2 = pre_mid.next