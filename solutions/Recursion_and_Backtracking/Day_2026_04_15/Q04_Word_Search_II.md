# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The words can be located horizontally, vertically, or diagonally in the grid.

## Approach
The approach involves using a Trie data structure to store the dictionary words and then using backtracking to search for each word in the grid. The Trie allows for efficient lookup and the backtracking ensures that all possible paths are explored.

## Complexity
- Time: O(N*M*4^L) where N and M are the dimensions of the grid and L is the maximum length of a word
- Space: O(N*M + T) where T is the total number of nodes in the Trie

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
                dfs(board, i, j, root, visited, result);
            }
        }
        return result;
    }

    void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, vector<vector<bool>>& visited, vector<string>& result) {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j] || node->children.find(board[i][j]) == node->children.end()) {
            return;
        }

        visited[i][j] = true;
        node = node->children[board[i][j]];
        if (!node->word.empty()) {
            result.push_back(node->word);
            node->word.clear();
        }

        dfs(board, i - 1, j, node, visited, result);
        dfs(board, i + 1, j, node, visited, result);
        dfs(board, i, j - 1, node, visited, result);
        dfs(board, i, j + 1, node, visited, result);
        dfs(board, i - 1, j - 1, node, visited, result);
        dfs(board, i - 1, j + 1, node, visited, result);
        dfs(board, i + 1, j - 1, node, visited, result);
        dfs(board, i + 1, j + 1, node, visited, result);

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
- Using a Trie data structure to store the dictionary words allows for efficient lookup.
- Backtracking is used to search for each word in the grid, exploring all possible paths.
- The `visited` matrix is used to keep track of visited cells and avoid revisiting them.