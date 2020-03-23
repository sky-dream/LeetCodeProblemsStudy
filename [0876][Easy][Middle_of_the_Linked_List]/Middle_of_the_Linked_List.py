# leetcode time     cost : 44 ms
# leetcode memory   cost : 13.3 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# solution 1, convert link list to list
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        print(A)
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

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