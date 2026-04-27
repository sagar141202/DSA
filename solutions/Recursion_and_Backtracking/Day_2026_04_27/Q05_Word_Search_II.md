# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The board contains only lowercase English letters. The input words are non-empty and contain only lowercase English letters. The dictionary may contain duplicate words, but the answer should not contain duplicate words.

## Approach
The approach to solve this problem is to use a Trie data structure to store the dictionary words and then use backtracking to search for each word in the grid. We iterate over each cell in the grid and for each cell, we check if the current character is present in the Trie. If it is, we recursively explore all possible words that can be formed from the current cell.

## Complexity
- Time: O(N * M * 4^L * D) where N is the number of rows, M is the number of columns, L is the maximum length of a word, and D is the number of words in the dictionary.
- Space: O(N * M + D) for storing the Trie and the visited cells.

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
Output: ["eat","oath"]
```

## Key Takeaways
- Use a Trie data structure to store the dictionary words for efficient lookup.
- Use backtracking to search for each word in the grid, exploring all possible directions from each cell.
- Keep track of visited cells to avoid revisiting the same cell in a word.