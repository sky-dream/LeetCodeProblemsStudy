# -*- coding: utf-8 -*-  
# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.7 MB
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# solution 2, fast and slow pointers, no extra memory needed,
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # find the linked list node count
        first = head
        n = 1
        while first.next:
            first = first.next
            n += 1
        k= k%n
        first = second = head
        # find the delta node count we need to move to the head part
        while(k):
            k-=1
            first=first.next
        # used slow pointer to find the new tail    
        while(first.next):
            first=first.next
            second=second.next
        # link old tail to the head to get the ring    
        first.next=head
        # update the new head
        head=second.next
        # break the ring
        second.next=None
        return head
    
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