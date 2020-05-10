# -*- coding: utf-8 -*-  
# leetcode time     cost : 36 ms
# leetcode memory   cost : 13.7 MB
# solution 1, sum formula dict and stack in sum() and set()
class Excel:
    def __init__(self, H: int, W: str):
        self.w = self.char_to_num(W)
        self.h = H
        self.nums = [[0]*(self.w+1) for _ in range (self.h+1)]
        # all row 0, all col 0 will not be used
        for i in range (1, self.h+1):
            self.nums[i][0] = i
        for i in range (1, self.w+1):
            self.nums[0][i] = chr(ord('A')+i-1)
        # sum formula dict,cell str('B23') is key, 
        # sum formula str('A2','B1:G12') is value
        self.prev_sum = {}

    def char_to_num(self, c):
        return ord(c)-ord('A')+1
    # get cell_str used counter in sum_formula_strs
    def in_strs(self, cell_str, sum_formula_strs):
        count = 0
        for string in sum_formula_strs:
            if string.find(':') == -1:
                if cell_str == string:
                    count += 1
            else:
                idx = string.find(':')+1
                # H->(1-26),W->(A-Z),eg:'B1:G12'
                if string[:1]<=cell_str[:1]<=string[idx:idx+1] and int(string[1:idx-1])<=int(cell_str[1:])<=int(string[idx+1:]):
                    count += 1
        return count

    def set(self, r: int, c: str, v: int) -> None:
        v_old = self.get(r, c)
        self.nums[r][self.char_to_num(c)] = v

        cell_str = c+str(r)
        if cell_str in self.prev_sum:
            del self.prev_sum[cell_str]

        if len(self.prev_sum) > 0:
            # stack used for formula dependency
            candidate = []
            while cell_str:
                # loop all cells that have sum formula.
                # update cells which sum is based on cell_str.
                for key in self.prev_sum:
                    if cell_str == key:
                        continue
                    cell_formula = self.prev_sum[key]
                    counter = self.in_strs(cell_str, cell_formula)
                    if counter > 0:
                        # H->(1-26),W->(A-Z),eg:'G12'
                        self.nums[int(key[1:])][self.char_to_num(key[0])] += counter*(v-v_old)
                        candidate.append(key)

                cell_str = None if not candidate else candidate.pop(-1)

    def get(self, r: int, c: str) -> int:
        return self.nums[r][self.char_to_num(c)]

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        self.prev_sum[c+str(r)] = [x for x in strs]

        sums = 0
        while strs:
            s = strs.pop(0)
            
            if s.find(':') == -1:
                # use s[1:] not s[1],eg:'G12'
                sums += self.nums[int(s[1:])][self.char_to_num(s[0])]
            # or formula is a cell range,eg:'B1:G12'
            else:
                # end cell str start index in sum formula list
                idx = s.find(':')+1 
                h_start = int(s[1:idx-1])
                w_start = self.char_to_num(s[0])
                
                h_end = int(s[idx+1:])
                w_end = self.char_to_num(s[idx])

                for i in range (h_start, h_end+1):
                    for j in range (w_start, w_end+1):
                        sums += self.nums[i][j]

        self.nums[r][self.char_to_num(c)] = sums
        return sums
        
# Your Excel object will be instantiated and called as such:
# obj = Excel(H, W)
# obj.set(r,c,v)
# param_2 = obj.get(r,c)
# param_3 = obj.sum(r,c,strs)