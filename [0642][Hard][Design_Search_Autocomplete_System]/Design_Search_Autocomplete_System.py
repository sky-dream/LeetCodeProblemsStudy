# -*- coding: utf-8 -*-  
# leetcode time     cost : 776 ms
# leetcode memory   cost : 19 MB
import heapq
class TrieNode:
    def __init__(self):
        self.nextDict = {}
        self.isWord = False
        self.times = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, times=1):
        cur = self.root
        for c in word:
            if c not in cur.nextDict:
                cur.nextDict[c] = TrieNode()
            cur = cur.nextDict[c]
        cur.isWord = True
        cur.times += times
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.nextDict:
                return []
            cur = cur.nextDict[c]
        res, inputStringBuffer = [], [word]
        self.dfs(cur, res, inputStringBuffer)
        return res
    
    def dfs(self, cur, res, inputStringBuffer):
        if cur.isWord:
            res.append((-cur.times, ''.join(inputStringBuffer)))
        for c in cur.nextDict:
            inputStringBuffer.append(c)
            self.dfs(cur.nextDict[c], res, inputStringBuffer)
            inputStringBuffer.pop()
    
class AutocompleteSystem:

    def __init__(self, sentences: [str], times: [int]):
        self.root = Trie()
        self.exists = True
        self.inputStringBuffer = ''
        for i in range(len(sentences)):
            self.root.insert(sentences[i], times[i])

    def input(self, c: str):
        if c == '#':
            self.root.insert(self.inputStringBuffer, 1)
            self.inputStringBuffer = ''
            self.exists = True
            return []
        else:
            self.inputStringBuffer += c
            if not self.exists:
                return []
            words = self.root.search(self.inputStringBuffer)
            if words:
                heapq.heapify(words)
                res = []
                while words and len(res) < 3:
                    res.append(heapq.heappop(words)[1])
                return res
            else:
                self.exists = False
                return []
        
# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)