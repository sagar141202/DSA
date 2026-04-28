# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given a board `[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]` and a word `"ABCCED"`, the output should be `true`. The board size will be at most 200x200 and the word length will be at most 200.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the grid and check if the word exists. It iterates over each cell in the grid and calls the DFS function to check if the word can be formed starting from that cell. The DFS function checks if the current character in the word matches the character in the current cell, and if so, it recursively calls itself for the adjacent cells.

## Complexity
- Time: O(N*M*4^L)
- Space: O(N*M + L)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, string& word, int i, int j, int k) {
        if (k == word.size()) {
            return true;
        }
        
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || word[k] != board[i][j]) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '#';
        
        bool found = dfs(board, word, i + 1, j, k + 1) ||
                      dfs(board, word, i - 1, j, k + 1) ||
                      dfs(board, word, i, j + 1, k + 1) ||
                      dfs(board, word, i, j - 1, k + 1);
        
        board[i][j] = temp;
        
        return found;
    }
};
```

## Test Cases
```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
```

## Key Takeaways
- Use DFS to traverse the grid and check if the word exists.
- Mark visited cells to avoid revisiting them.
- Restore the original state of the grid after the DFS traversal.