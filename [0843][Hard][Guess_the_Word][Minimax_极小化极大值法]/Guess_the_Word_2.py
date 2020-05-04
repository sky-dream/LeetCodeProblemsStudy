# leetcode time     cost : 100 ms
# leetcode memory   cost : 13.9 MB 
# Time  Complexity: O(N**2*logN)
# Space Complexity: O(N**2)
# solution 1,MiniMax
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

# solution 1, 启发式极小化极大算法
class Solution(object):
    # def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
    def findSecretWord(self, wordlist, master):
        N = len(wordlist)
        # python3中filter,map,zip本身就已经是generator了,无需再调用 python2, itertools.izip
        self.H = [[sum(a==b for a,b in zip(wordlist[i], wordlist[j]))
                   for j in range(N)] for i in range(N)]

        possible, path = range(N), ()
        while possible:
            guess = self.solve(possible, path)
            matches = master.guess(wordlist[guess])
            if matches == len(wordlist[0]): return
            possible = [j for j in possible if self.H[guess][j] == matches]
            path = path + (guess,)

    def solve(self, possible, path = ()):
        if len(possible) <= 2: return possible[0]

        ansgrp, ansguess = possible, None
        for guess, row in enumerate(self.H):
            if guess not in path:
                groups = [[] for _ in range(7)]
                for j in possible:
                    if j != guess:
                        groups[row[j]].append(j)
                maxgroup = max(groups, key = len)
                if len(maxgroup) < len(ansgrp):
                    ansgrp, ansguess = maxgroup, guess

        return ansguess