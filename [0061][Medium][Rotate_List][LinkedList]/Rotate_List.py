# -*- coding: utf-8 -*-  
# leetcode time     cost : 32 ms
# leetcode memory   cost : 13.7 MB
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# solution 1, loop the linked list twice, no extra memory needed,
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head
        
        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - (k % n) - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        return new_head
    
def listToListNode(numbers: 'List') -> 'ListNode':

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToList(node):
    if not node:
        return []
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
def main():
    head,k = [1,2,3,4,5],2
    head =  listToListNode(head)
    expect = [4,5,1,2,3]
    obj = Solution()
    result = obj.rotateRight(head,k)
    result = listNodeToList(result)
    try:
        assert result == expect
        print("passed, result is follow expectation:",result)
    except AssertionError as aError:
        print('failed, result is wrong',result, aError.__str__())
    
if __name__ =='__main__':
    main()   