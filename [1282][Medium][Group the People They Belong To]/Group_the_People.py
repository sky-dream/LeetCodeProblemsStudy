class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        res = []
        groupx = dict()
        for i in range(len(groupSizes)):
            if groupSizes[i] not in groupx.keys():
                groupx[groupSizes[i]] =[]                
            groupx[groupSizes[i]].append(i) 
            if (len(groupx[groupSizes[i]]) == groupSizes[i]):
                res.append(groupx[groupSizes[i]])
                groupx[groupSizes[i]] = []            
        return res
groupSizes = [3,3,3,3,3,1,3]
s = Solution()
print(s.groupThePeople(groupSizes))