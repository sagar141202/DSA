# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given a board `[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]` and a word `"ABCCED"`, the output should be `true`. The board has a size of `m x n`, where `m` and `n` are the number of rows and columns respectively.

## Approach
The algorithm uses a depth-first search (DFS) approach to traverse the grid and find the word. It checks all possible directions (up, down, left, right) from each cell to find a match. The search is performed recursively, and the function backtracks when it cannot find a match.

## Complexity
- Time: O(N * M * 4^L)
- Space: O(N * M + L)

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
    
    bool dfs(vector<vector<char>>& board, string word, int i, int j, int k) {
        int m = board.size();
        int n = board[0].size();
        
        if (k == word.size()) {
            return true;
        }
        
        if (i < 0 || i >= m || j < 0 || j >= n || word[k] != board[i][j]) {
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
- Use DFS to traverse the grid and find the word.
- Backtrack when a dead end is reached to explore other possibilities.
- Mark visited cells to avoid revisiting them and entering an infinite loop.