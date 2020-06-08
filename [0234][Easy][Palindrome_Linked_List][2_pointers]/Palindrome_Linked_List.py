# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# leetcode time     cost : 132 ms
# leetcode memory   cost : 24.1 MB 
# Time  Complexity: O(n)
# Space Complexity: O(n)
# solution 1, with a extra array
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]