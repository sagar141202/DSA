# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The words can be found in any direction (horizontally, vertically, or diagonally).

## Approach
The solution uses a Trie data structure to store the dictionary words and then performs a depth-first search on the board to find all words. The Trie allows for efficient lookup of words, while the depth-first search explores all possible paths on the board.

## Complexity
- Time: O(N*M*4^L), where N is the number of rows, M is the number of columns, and L is the maximum length of a word
- Space: O(N*M + W), where W is the total number of words in the dictionary

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
Input: board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

## Key Takeaways
- Use a Trie data structure to store dictionary words for efficient lookup
- Perform depth-first search on the board to find all words
- Use a visited matrix to avoid revisiting the same cell multiple times