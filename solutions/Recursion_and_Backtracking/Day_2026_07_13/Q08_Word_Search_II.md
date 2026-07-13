# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. Example: 
Input: 
board = [
    ["o","a","a","n"],
    ["e","t","a","e"],
    ["i","h","k","r"],
    ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

## Approach
The algorithm uses a Trie data structure to store the dictionary words and then performs a depth-first search (DFS) on the board to find all words. The DFS is guided by the Trie to prune branches that do not lead to a word in the dictionary. 
This approach ensures that we explore all possible words in the board efficiently.

## Complexity
- Time: O(N * M * 4^L), where N and M are the dimensions of the board, and L is the maximum length of a word.
- Space: O(N * M + W), where W is the total number of characters in all words.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct TrieNode {
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
- Use a Trie to store dictionary words for efficient lookup.
- Perform DFS on the board to find all words, guided by the Trie to prune branches.
- Use a visited matrix to avoid revisiting cells and to ensure that each word is constructed from distinct cells.