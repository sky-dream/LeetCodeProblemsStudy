# solution 1, back tracking.
# leetcode time     cost : 144 ms
# leetcode memory   cost : 13.2 MB 
# Time  Complexity: O(1)
# Space Complexity: O(1)
'''
   The AC-3 algorithm (short for Arc Consistency Algorithm #3) is one of a series of algorithms 
used for the solution of constraint satisfaction problems (or CSP's). It was developed by Alan Mackworth in 1977. 
The earlier AC algorithms are often considered too inefficient, and many of the later ones are difficult to implement, 
and so AC-3 is the one most often taught and used in very simple constraint solvers.

related link:
https://en.wikipedia.org/wiki/AC-3_algorithm,
https://blog.csdn.net/tianhan4/article/details/19991899
'''
class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        (row_sets, col_sets, sec_sets, fill_set) = self.findRowColSecSets(board)
        (row_empty, col_empty, sec_empty, candidate_dict) = self.findCandidates(row_sets, col_sets, sec_sets, fill_set)
        self.ac3(fill_set, candidate_dict, row_empty, col_empty, sec_empty)
        determined = []
        # fill_set = self.sortFillSet(fill_set, candidate_dict)
        if self.dfs(fill_set, candidate_dict, row_empty, col_empty, sec_empty, determined):
            for each in determined:
                board[each[0][0]][each[0][1]] = str(each[1])
    
    # A final step recursive dfs
    def dfs(self, fill_set, candidat_dict, row_empty, col_empty, sec_empty, determined):
        if len(fill_set) == 0:
            return True
        for each_value in candidat_dict[fill_set[0]]:
            copy_candidate_dict = self.copyDict(candidat_dict)
            copy_row_empty = self.copyDict(row_empty)
            copy_row_empty[fill_set[0][0]].remove(fill_set[0][1])
            copy_col_empty = self.copyDict(col_empty)
            copy_col_empty[fill_set[0][1]].remove(fill_set[0][0])
            copy_sec_empty = self.copyDict(sec_empty)
            section_idx = 3*int(fill_set[0][0]/3) + int(fill_set[0][1]/3)
            copy_sec_empty[section_idx].remove(fill_set[0])
            del copy_candidate_dict[fill_set[0]]
            for each_element in copy_row_empty[fill_set[0][0]]:
                if each_value in copy_candidate_dict[(fill_set[0][0], each_element)]:
                    copy_candidate_dict[(fill_set[0][0], each_element)].remove(each_value)
            for each_element in copy_col_empty[fill_set[0][1]]:
                if each_value in copy_candidate_dict[(each_element, fill_set[0][1])]:
                    copy_candidate_dict[(each_element, fill_set[0][1])].remove(each_value)
            for each_element in copy_sec_empty[section_idx]:
                if each_value in copy_candidate_dict[each_element]:
                    copy_candidate_dict[each_element].remove(each_value)
            determined.append((fill_set[0], each_value))
            if self.dfs(fill_set[1:], copy_candidate_dict, copy_row_empty, copy_col_empty, copy_sec_empty, determined):
                return True
            else:
                del determined[-1]
        return False
    
    # Find the possible set of number that left out for each row, column and sub square    
    def findRowColSecSets(self, board):
        row_sets = [set(range(1,10)) for i in range(9)]
        col_sets = [set(range(1,10)) for i in range(9)]
        sec_sets = [set(range(1,10)) for i in range(9)]
        fill_set = []
        for row_idx, eachrow in enumerate(board):
            for col_idx, each in enumerate(eachrow):
                if each != ".":
                    row_sets[row_idx].remove(int(each))
                    col_sets[col_idx].remove(int(each))
                    sec_sets[3*int(row_idx/3) + int(col_idx/3)].remove(int(each))
                else:
                    fill_set.append((row_idx,col_idx))
        return (row_sets, col_sets, sec_sets, fill_set)

    # Find possible set of numbers for each empty position
    def findCandidates(self, row_sets, col_sets, sec_sets, fill_set):
        row_empty = {}
        col_empty = {}
        sec_empty = {}
        candidate_dict = {}
        for each_pair in fill_set:
            section_idx = 3*int(each_pair[0]/3) + int(each_pair[1]/3)
            candidate_dict[each_pair] = set()
            for x in range(1,10):
                if x in row_sets[each_pair[0]] and x in col_sets[each_pair[1]] and x in sec_sets[section_idx]:
                    candidate_dict[each_pair].add(x)
            if each_pair[0] in row_empty:
                row_empty[each_pair[0]].add(each_pair[1])
            else:
                row_empty[each_pair[0]] = set([each_pair[1]])
            if each_pair[1] in col_empty:
                col_empty[each_pair[1]].add(each_pair[0])
            else:
                col_empty[each_pair[1]] = set([each_pair[0]])
            if section_idx in sec_empty:
                sec_empty[section_idx].add(each_pair)
            else:
                sec_empty[section_idx] = set([each_pair])
        return (row_empty, col_empty, sec_empty, candidate_dict)
   
    def copyDict(self, a_dict):
        return {key:set(a_dict[key]) for key in a_dict}
    
    # AC-3 constraint checking
    def ac3(self, fill_set, candidat_dict, row_empty, col_empty, sec_empty):
        queue = list(fill_set)
        while len(queue) > 0:
            each_candidate = queue[0]
            simplified_list = []
            for each_value in candidat_dict[each_candidate]:
                other = False
                for each_place in row_empty[each_candidate[0]]:
                    if each_place != each_candidate[1] and (each_value in candidat_dict[(each_candidate[0], each_place)]):
                        other = True
                        break
                if not other:
                    simplified_list.append(each_value)
                    continue
                other = False
                for each_place in col_empty[each_candidate[1]]:
                    if each_place != each_candidate[0] and (each_value in candidat_dict[(each_place, each_candidate[1])]):
                        other = True
                        break
                if not other:
                    simplified_list.append(each_value)
                    continue
                other = False
                for each_place in sec_empty[3*int(each_candidate[0]/3) + int(each_candidate[1]/3)]:
                    if each_place != each_candidate and (each_value in candidat_dict[each_place]):
                        other = True
                        break
                if not other:
                    simplified_list.append(each_value)
            if len(simplified_list) > 0:
                if len(simplified_list) < len(candidat_dict[each_candidate]):
                    candidat_dict[each_candidate] = set(simplified_list)
                    for each_place in row_empty[each_candidate[0]]:
                        if each_place != each_candidate[1]:
                            queue.append((each_candidate[0], each_place))
                    for each_place in col_empty[each_candidate[1]]:
                        if each_place != each_candidate[0]:
                            queue.append((each_place, each_candidate[1]))
                    for each_place in sec_empty[3*int(each_candidate[0]/3) + int(each_candidate[1]/3)]:
                        if each_place != each_candidate:
                            queue.append(each_place)
            del queue[0]