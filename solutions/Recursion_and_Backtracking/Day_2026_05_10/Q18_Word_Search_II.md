# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The words can be located horizontally, vertically, or diagonally.

## Approach
The solution uses a Trie data structure to store the dictionary words and a Depth-First Search (DFS) algorithm to explore the board. The algorithm checks each cell in the board as a potential starting point for a word and uses the Trie to efficiently prune the search space.

## Complexity
- Time: O(N * M * 4^L)
- Space: O(N * M + D)

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
        int n = board.size();
        int m = board[0].size();
        TrieNode* root = new TrieNode();
        for (string word : words) {
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
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
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
        dfs(board, node, i - 1, j - 1, visited, result);
        dfs(board, node, i + 1, j - 1, visited, result);
        dfs(board, node, i - 1, j + 1, visited, result);
        
        visited[i][j] = false;
    }
};

```

## Test Cases
```
Input: board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

## Key Takeaways
- Use a Trie to efficiently store and search for words in the dictionary.
- Implement a Depth-First Search (DFS) algorithm to explore the board and find words.
- Use a visited matrix to avoid revisiting the same cell multiple times.