# solution 1 greedy algorithm.
# leetcode time     cost : 136 ms
# leetcode memory   cost : 12.1 MB 
# Time  Complexity: O(N)
# Space Complexity: O(1)
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0

        for cmd in commands:
            if cmd == -2:  #left
                di = (di - 1) % 4
            elif cmd == -1:  #right
                di = (di + 1) % 4
            else:
                for k in range(cmd):
                    if (x+dx[di], y+dy[di]) not in obstacleSet:
                        x += dx[di]
                        y += dy[di]
                        ans = max(ans, x*x + y*y)

        return ans
    
def main():
    commands = [4,-1,4,-2,4]
    obstacles = [[2,4]]         # will be stucked in  (1, 4) before go to (1, 8) expect res is 65
    obj = Solution()
    res = obj.robotSim(commands, obstacles)
    print("return value is "+str(res));
    
if __name__ =='__main__':
    main()     