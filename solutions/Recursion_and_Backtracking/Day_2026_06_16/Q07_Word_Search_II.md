# Word Search II

## Problem Statement
Given a 2D board and a list of words from the dictionary, find all words in the board. Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word. The words can be found in any direction (horizontally, vertically, or diagonally). The input will be a 2D array of characters and an array of strings. The output should be a list of all the words found in the board.

## Approach
The solution uses a combination of Depth-First Search (DFS) and Trie data structure to efficiently find all words in the board. The Trie is used to store the dictionary words, and DFS is used to explore all possible paths from each cell in the board.

## Complexity
- Time: O(N * M * 4^L * W)
- Space: O(N * M + W)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class TrieNode {
public:
    unordered_map<char, TrieNode*> children;
    string word;
    TrieNode() {}
};

class Solution {
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        int n = board.size();
        int m = board[0].size();
        vector<string> result;
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
        
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        vector<int> dx = {-1, 1, 0, 0};
        vector<int> dy = {0, 0, -1, 1};
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dfs(board, i, j, root, result, visited, dx, dy);
            }
        }
        
        return result;
    }
    
    void dfs(vector<vector<char>>& board, int x, int y, TrieNode* node, vector<string>& result, vector<vector<bool>>& visited, vector<int>& dx, vector<int>& dy) {
        if (node->word != "") {
            result.push_back(node->word);
            node->word = "";
        }
        
        visited[x][y] = true;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            if (nx >= 0 && nx < board.size() && ny >= 0 && ny < board[0].size() && !visited[nx][ny] && node->children.find(board[nx][ny]) != node->children.end()) {
                dfs(board, nx, ny, node->children[board[nx][ny]], result, visited, dx, dy);
            }
        }
        visited[x][y] = false;
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
        cout << word << " ";
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
]
words = ["oath", "pea", "eat", "rain"]
Output: ["oath", "eat"]
```

## Key Takeaways
- Use a Trie data structure to store the dictionary words for efficient lookup.
- Use Depth-First Search (DFS) to explore all possible paths from each cell in the board.
- Use a visited array to keep track of visited cells and avoid revisiting them.