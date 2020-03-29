# leetcode time     cost : --- ms,max time exceeded
# leetcode memory   cost : --- MB 
# Time  Complexity: O(8**k)
# Space Complexity: O(N*N)
# solution 1, BFS, add(row,col,layer,possibility) into the queue, init is the (r,c,1)
# get (pos_x,pos_y,prev_possible) from the queue for the bfs start
# count the still on board num, curr_possible = prev_possible/8,
# append the curr_possible to the dict list of the all layer possibles
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        directions = [[-2,1],[-2,-1],[2,-1],[2,1],[-1,-2],[1,-2],[-1,2],[1,2]]
        queue = []
        possible_list_dict= {}
        for i in range(K+1):
            possible_list_dict[i+1] = []
        if K==0:
            return 1
        if N<=2:
            return 0
        queue.append((r,c,1,1))
        def isOnBoard(r,c):
            return 0<=r<N and 0<=c<N

        while queue:
            onBoardCount = 0
            r,c,layer,p = queue.pop(0)
            if layer > K:
                break
            for direct in directions:
                new_r = r + direct[0]
                new_c = c + direct[1]
                if isOnBoard(new_r,new_c):
                    onBoardCount+=1
                    queue.append((new_r,new_c,layer+1,p/8))
                    possible_list_dict[layer].append(p/8)
        if len(possible_list_dict[K]):
            return sum(possible_list_dict[K])
        else:
            return 0

def main():
    N, K, r, c = 3,4,0,0 #expect is 0.00390625
    obj = Solution()
    result = obj.knightProbability(N, K, r, c)
    print("return result is ",result);

if __name__ =='__main__':
    main() 