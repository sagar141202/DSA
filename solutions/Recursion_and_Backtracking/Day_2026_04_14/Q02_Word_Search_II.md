# Word Search II

## Problem Statement
Given a 2D board and a list of words from a dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The words can be found in any direction (horizontally, vertically, or diagonally).

## Approach
The solution uses a combination of recursion and backtracking to explore all possible paths in the grid. A Trie data structure is used to efficiently store and look up words. The algorithm iterates over each cell in the grid, using the Trie to guide the search for words.

## Complexity
- Time: O(N * M * 4^L), where N is the number of rows, M is the number of columns, and L is the maximum length of a word
- Space: O(N * M + W), where W is the total number of words in the dictionary

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

        set<string> result;
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                dfs(board, root, i, j, result);
            }
        }
        return vector<string>(result.begin(), result.end());
    }

    void dfs(vector<vector<char>>& board, TrieNode* node, int i, int j, set<string>& result) {
        char c = board[i][j];
        if (node->children.find(c) == node->children.end()) return;
        node = node->children[c];
        if (!node->word.empty()) {
            result.insert(node->word);
            node->word.clear();
        }
        board[i][j] = '#';
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        for (const auto& dir : directions) {
            int ni = i + dir.first, nj = j + dir.second;
            if (ni >= 0 && ni < board.size() && nj >= 0 && nj < board[0].size() && board[ni][nj] != '#') {
                dfs(board, node, ni, nj, result);
            }
        }
        board[i][j] = c;
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
    for (const string& word : result) {
        cout << word << " ";
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
Output: ["oath","eat"]
```

## Key Takeaways
- Use a Trie to efficiently store and look up words
- Use recursion and backtracking to explore all possible paths in the grid
- Avoid revisiting cells by marking them as visited during the search process