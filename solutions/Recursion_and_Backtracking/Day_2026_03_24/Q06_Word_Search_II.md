# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where adjacent cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The input will be a 2D array of characters board and an array of strings words. The output should be a list of strings, which are the words found in the board. For example, given the following board and words: 
board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]
The function should return ["eat","oath"].

## Approach
The algorithm uses a combination of recursion and backtracking to find all words in the board. It iterates over each cell in the board and attempts to construct a word from that cell. The algorithm checks if the current character in the board matches the first character of any word in the dictionary, and if so, it recursively checks the neighboring cells to construct the rest of the word.

## Complexity
- Time: O(N * M * 4^L), where N is the number of rows in the board, M is the number of columns, and L is the maximum length of a word.
- Space: O(N * M + W), where W is the total number of characters in all words.

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
                dfs(board, i, j, root, result, visited);
            }
        }
        return result;
    }

    void dfs(vector<vector<char>>& board, int i, int j, TrieNode* node, vector<string>& result, vector<vector<bool>>& visited) {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j] || node->children.find(board[i][j]) == node->children.end()) {
            return;
        }

        visited[i][j] = true;
        node = node->children[board[i][j]];
        if (!node->word.empty()) {
            result.push_back(node->word);
            node->word.clear();
        }

        dfs(board, i - 1, j, node, result, visited);
        dfs(board, i + 1, j, node, result, visited);
        dfs(board, i, j - 1, node, result, visited);
        dfs(board, i, j + 1, node, result, visited);

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
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
```

## Key Takeaways
- The Trie data structure is used to store the dictionary words for efficient lookup.
- The dfs function is used to perform a depth-first search on the board, exploring all possible paths from each cell.
- The visited array is used to keep track of visited cells and avoid revisiting them.