# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The words can be located horizontally, vertically, or diagonally in the grid. The input will be a 2D array of characters `board`, and a list of strings `words`. The output will be a list of strings, which are the words found in the board.

## Approach
The solution uses a Trie data structure to store the dictionary words, and then uses backtracking to search for each word in the grid. The algorithm iterates over each cell in the grid, and for each cell, it checks if the cell's letter is in the Trie. If it is, the algorithm continues to explore adjacent cells.

## Complexity
- Time: O(N * M * 4^L * W) where N is the number of rows, M is the number of columns, L is the maximum length of a word, and W is the number of words.
- Space: O(N * M + W) for the Trie and the visited set.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    string word;
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        TrieNode* root = new TrieNode();
        for (const string& word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (node->children.find(c) == node->children.end()) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->word = word;
        }
        
        vector<string> result;
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                dfs(board, root, i, j, visited, result);
            }
        }
        return result;
    }
    
    void dfs(vector<vector<char>>& board, TrieNode* node, int i, int j, vector<vector<bool>>& visited, vector<string>& result) {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j] || node->children.find(board[i][j]) == node->children.end()) {
            return;
        }
        
        visited[i][j] = true;
        node = node->children[board[i][j]];
        if (!node->word.empty()) {
            result.push_back(node->word);
            node->word.clear();
        }
        
        dfs(board, node, i + 1, j, visited, result);
        dfs(board, node, i - 1, j, visited, result);
        dfs(board, node, i, j + 1, visited, result);
        dfs(board, node, i, j - 1, visited, result);
        dfs(board, node, i + 1, j + 1, visited, result);
        dfs(board, node, i + 1, j - 1, visited, result);
        dfs(board, node, i - 1, j + 1, visited, result);
        dfs(board, node, i - 1, j - 1, visited, result);
        
        visited[i][j] = false;
    }
};

```

## Test Cases
```
Input: 
board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
],
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

## Key Takeaways
- Use a Trie data structure to store the dictionary words for efficient lookup.
- Use backtracking to search for each word in the grid, exploring all possible paths from each cell.
- Keep track of visited cells to avoid revisiting the same cell in a word.