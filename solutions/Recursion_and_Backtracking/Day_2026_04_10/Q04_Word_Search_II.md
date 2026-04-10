# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where adjacent cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The words can be located horizontally, vertically, or diagonally in the grid. We need to find all the words from the dictionary that can be formed using the letters of the grid.

## Approach
The approach is to use a Trie data structure to store the dictionary words and then use backtracking to explore all possible paths in the grid. We start by inserting all the dictionary words into the Trie, and then for each cell in the grid, we use backtracking to explore all possible words that can be formed starting from that cell.

## Complexity
- Time: O(N * M * 4^L * W) where N is the number of rows, M is the number of columns, L is the maximum length of a word, and W is the number of words in the dictionary.
- Space: O(N * M + W) for the grid and the Trie.

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
        dfs(board, node, i - 1, j, visited, result);
        dfs(board, node, i + 1, j, visited, result);
        dfs(board, node, i, j - 1, visited, result);
        dfs(board, node, i, j + 1, visited, result);
        dfs(board, node, i - 1, j - 1, visited, result);
        dfs(board, node, i - 1, j + 1, visited, result);
        dfs(board, node, i + 1, j - 1, visited, result);
        dfs(board, node, i + 1, j + 1, visited, result);
        visited[i][j] = false;
    }
};

int main() {
    Solution solution;
    vector<vector<char>> board = {
        {'o', 'a', 'a', 'n'},
        {'e', 't', 'a', 'e'},
        {'i', 'h', 'k', 'r'},
        {'i', 'f', 'l', 'v'}
    };
    vector<string> words = {"oath", "pea", "eat", "rain"};
    vector<string> result = solution.findWords(board, words);
    for (string word : result) {
        cout << word << endl;
    }
    return 0;
}
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
Output: 
["eat","oath"]
```

## Key Takeaways
- We use a Trie to store the dictionary words for efficient lookup.
- We use backtracking to explore all possible paths in the grid.
- We mark visited cells to avoid revisiting them and to ensure that each cell is used at most once in a word.