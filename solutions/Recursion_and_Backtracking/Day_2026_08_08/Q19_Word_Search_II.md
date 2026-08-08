# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The board contains only lowercase English letters. The input words are non-empty and contain only lowercase English letters.

## Approach
We will use a Trie data structure to store the words and then use backtracking to explore all possible paths in the board. The Trie will help us to efficiently check if a word is present in the dictionary. We will start from each cell in the board and try to form a word by exploring all adjacent cells.

## Complexity
- Time: O(N*M*4^L), where N is the number of rows, M is the number of columns, and L is the maximum length of a word.
- Space: O(N*M + W), where W is the total number of words in the dictionary.

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
Output: ["eat","oath"]
```

## Key Takeaways
- Use a Trie data structure to store the words for efficient lookup.
- Use backtracking to explore all possible paths in the board.
- Mark visited cells to avoid revisiting them and to ensure that each cell is used at most once in a word.