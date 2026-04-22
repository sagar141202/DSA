# Word Search II

## Problem Statement
Given a 2D board and a list of words from a dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

## Approach
The approach is to use a Trie data structure to store the dictionary words and then use depth-first search (DFS) with backtracking to find all words in the board. For each cell in the board, we start a DFS from that cell and explore all possible paths.

## Complexity
- Time: O(N * M * 4^L), where N and M are the dimensions of the board and L is the maximum length of a word
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

        node = node->children[board[i][j]];
        if (!node->word.empty()) {
            result.push_back(node->word);
            node->word.clear();
        }

        visited[i][j] = true;
        dfs(board, i - 1, j, node, visited, result);
        dfs(board, i + 1, j, node, visited, result);
        dfs(board, i, j - 1, node, visited, result);
        dfs(board, i, j + 1, node, visited, result);
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
    ['o', 'a', 'a', 'n'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
],
words = ["oath", "pea", "eat", "rain"]
Output: ["oath", "eat"]
```

## Key Takeaways
- Use a Trie data structure to store the dictionary words for efficient lookup.
- Use DFS with backtracking to explore all possible paths in the board.
- Keep track of visited cells to avoid revisiting the same cell multiple times.