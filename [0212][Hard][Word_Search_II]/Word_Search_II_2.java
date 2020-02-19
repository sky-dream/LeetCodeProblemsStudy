//https://leetcode.com/problems/word-search-ii/discuss/59780/Java-15ms-Easiest-Solution-(100.00)
// leetcode time     cost : 9 ms
// leetcode memory   cost : 47.8 MB 

/*
Idea: The brute-force solution is to DFS all cells for every word in the dictionary. The time complexity will be O(m * n * wl * l) where 
m is board.length, n is board[0].length, l is words.length and wl is the average of length of words in 'words'.

Instead, we use a Trie to check multiple words at the same time when DFS from a certain cell.

Complexity - 
Time: O(m * n * wl * l) = max(O(wl * l), O(m * n * l * wl)) where
O(wl * l) - Build the trie
O(m * n * wl * l) - In the worst case where all words start with different chracters, and there is a word starting with a character
in the cell board[m - 1][n - 1], we have O(m * n * wl * l). However, if there are words starting with same characters and paths sharing
cells, Trie can check multiple words when DFS from a certain cell, rather than check ONLY ONE word when DFS from a certain cell like the 
brute-force solution.

Space: O(wl * l) = max(O(wl), O(wl * l)) where
O(wl) - The recursive stack can grow at most to wl layers. 
O(wl * l) - In the worst case when all words start with different characters, the trie has wl * l nodes. Also, since each word
is stored in a leaf node, all the leaf nodes require wl * l memory.
*/
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
class Solution {
    private List<String> result = new ArrayList<>();
	
    public List<String> findWords(char[][] board, String[] words) {
        if (board == null || words == null || words.length == 0) {
            return result;
        }
        
        TrieNode root = buildTrie(words);
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                recursiveFindWords(board, root, i, j);
                //System.out.println("findWords,result is  :" + result+", i :" + i+", j: "+j+",char: "+board[i][j]);
            }
        }
        
        return this.result;
    }
    
    private void recursiveFindWords(char[][] board, TrieNode parent, int x, int y) {   
        if (outOfBounds(board, x, y) || board[x][y] == '#' || parent.children.get(board[x][y]) == null) {
            return; // return if out of bounds, if visited and if current cell is not a character in the trie
        }
        
        char xy = board[x][y];
        TrieNode child = parent.children.get(xy);
        if (child.isEndOfWord) { // Found a word
            this.result.add(child.word);
            //System.out.println("recursiveFindWords,result is  :" + result);
            child.isEndOfWord = false; // Set to false to avoid adding word to result multiple times
            // Don't RETURN since child.word can be a prefix of other words, e.g., 'ane' and 'aneis'
            //board[x][y] = '#'; // '#' marks a cell as visited 
        }
        
        
        
        recursiveFindWords(board, child, x, y - 1); // left
        recursiveFindWords(board, child, x - 1, y); // up
        recursiveFindWords(board, child, x, y + 1); // right
        recursiveFindWords(board, child, x + 1, y); // down
        
        board[x][y] = xy; // Set as unvisited since we are about to backtracking
    }
    
    private boolean outOfBounds(char[][] board, int x, int y) {
        return x < 0 || x >= board.length || y < 0 || y >= board[0].length;
    }
    
    // The trie is represented by a root node, not a Trie object
    private TrieNode buildTrie(String[] words) {
        TrieNode root = new TrieNode();
        for (String word : words) {
            if (word == null || word.isEmpty()) {
                continue;
            }
            
            TrieNode parent = root;
            for (int i = 0; i < word.length(); i++) {
                char cur = word.charAt(i);
                
                TrieNode child = parent.children.get(cur);
                if (child == null) {
                    child = new TrieNode();
                    parent.children.put(cur, child);
                }
                
                parent = child;
            }
            parent.isEndOfWord = true;
            parent.word = word; // Store a word at the leaf node
        }
        
        return root;
    }
    
    private class TrieNode {
        boolean isEndOfWord; // this.word is null if isEndOfWord is false
        String word; // Store the word so that no StringBuilder is needed to build the word char by char
        Map<Character, TrieNode> children;
        
        TrieNode() {
            this.children = new HashMap<>();
        }
    }
}

public class Word_Search_II_2 {
    public static void main(String args[]) {
        char[][] board = {{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}}; 
        String[] words = {"oath","pea","eat","rain"};                     // #expect is ["oath","eat"]
        Solution Solution_obj = new Solution();
        List<String> result = Solution_obj.findWords(board, words);
        System.out.println("In java code,return value is :" + (result));
    }
}