# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where adjacent cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The board contains only lowercase English letters. The input will contain at least one word.

## Approach
We can use a Trie data structure to store all the words and then use a depth-first search (DFS) approach to find all the words in the board. The DFS will explore all possible paths from each cell in the board and check if the current path forms a word in the Trie.

## Complexity
- Time: O(N*M*4^L), where N and M are the dimensions of the board and L is the maximum length of a word.
- Space: O(N*M + W), where W is the total number of words.

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
        for (string word : words) {
            TrieNode* node = root;
            for (char c : word) {
                if (!node->children.count(c)) {
                    node->children[c] = new TrieNode();
                }
                node = node->children[c];
            }
            node->word = word;
        }
        
        set<string> result;
        vector<vector<bool>> visited(board.size(), vector<bool>(board[0].size(), false));
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                dfs(board, i, j, root, result, visited);
            }
        }
        return vector<string>(result.begin(), result.end());
    }
    
    void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, set<string>& result, vector<vector<bool>>& visited) {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j] || !node->children.count(board[i][j])) {
            return;
        }
        visited[i][j] = true;
        node = node->children[board[i][j]];
        if (!node->word.empty()) {
            result.insert(node->word);
        }
        dfs(board, i-1, j, node, result, visited);
        dfs(board, i+1, j, node, result, visited);
        dfs(board, i, j-1, node, result, visited);
        dfs(board, i, j+1, node, result, visited);
        visited[i][j] = false;
    }
};
```

## Test Cases
```
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

## Key Takeaways
- Use a Trie data structure to store all the words for efficient lookup.
- Use a depth-first search (DFS) approach to explore all possible paths from each cell in the board.
- Keep track of visited cells to avoid using the same cell multiple times in a word.