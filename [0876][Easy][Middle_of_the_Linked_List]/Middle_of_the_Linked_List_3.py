# leetcode time     cost : 136 ms
# leetcode memory   cost : 12.1 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# solution 3, fast and slow pointer
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def stringToListNode(numbers):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr
   
def main():
    numbers = [1,2,3,4,5]       # 3
    head = stringToListNode(numbers)         
    obj = Solution()
    res = obj.middleNode(head)
    print("return value is ",res.val)
        
    
if __name__ =='__main__':
    main()     