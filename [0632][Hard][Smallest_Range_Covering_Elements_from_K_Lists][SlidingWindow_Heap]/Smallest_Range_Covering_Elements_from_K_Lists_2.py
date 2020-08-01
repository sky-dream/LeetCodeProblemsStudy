# -*- coding: utf-8 -*-  
# solution 2, hash table and 2 pointers
# Time  Complexity: O(N*k+V),N is the list length, k is the count of lists,V is the element value range
# Space Complexity: O(N*k)
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        # key is the value in list, dict value is the list No. which include this element
        indices = collections.defaultdict(list)
        xMin, xMax = 10**9, -10**9
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
            xMin = min(xMin, *vec)
            xMax = max(xMax, *vec)
        
        freq = [0] * n
        inside = 0
        left, right = xMin, xMin - 1
        bestLeft, bestRight = xMin, xMax

        while right < xMax:
            right += 1
            if right in indices:
                # key is the element value in list, dict value is the list No. which include this element
                for x in indices[right]:
                    freq[x] += 1
                    if freq[x] == 1:
                        inside += 1
                while inside == n:
                    if right - left < bestRight - bestLeft:
                        bestLeft, bestRight = left, right
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [bestLeft, bestRight]