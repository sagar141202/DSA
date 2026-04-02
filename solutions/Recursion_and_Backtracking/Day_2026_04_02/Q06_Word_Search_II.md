# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where adjacent cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The words can be located horizontally, vertically, or diagonally in the grid.

## Approach
The solution uses a Trie data structure to store the dictionary words, and then applies a depth-first search (DFS) with backtracking to explore all possible paths in the board. This approach ensures that each cell in the board is visited at most once for each word.

## Complexity
- Time: O(N*M*4^L), where N and M are the dimensions of the board, and L is the maximum length of a word in the dictionary.
- Space: O(N*M + D), where D is the total number of nodes in the Trie.

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
                dfs(board, i, j, root, result, visited);
            }
        }
        return result;
    }

    void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, vector<string>& result, vector<vector<bool>>& visited) {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j] || node->children.find(board[i][j]) == node->children.end()) {
            return;
        }

        node = node->children[board[i][j]];
        if (!node->word.empty()) {
            result.push_back(node->word);
            node->word.clear();
        }

        visited[i][j] = true;
        dfs(board, i + 1, j, node, result, visited);
        dfs(board, i - 1, j, node, result, visited);
        dfs(board, i, j + 1, node, result, visited);
        dfs(board, i, j - 1, node, result, visited);
        dfs(board, i + 1, j + 1, node, result, visited);
        dfs(board, i + 1, j - 1, node, result, visited);
        dfs(board, i - 1, j + 1, node, result, visited);
        dfs(board, i - 1, j - 1, node, result, visited);
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
- Using a Trie data structure can significantly reduce the time complexity of the solution by avoiding unnecessary string comparisons.
- The DFS with backtracking approach allows us to explore all possible paths in the board while avoiding revisiting the same cell multiple times for each word.
- The `visited` matrix is used to keep track of the cells that have been visited for each word, ensuring that each cell is used at most once in each word.