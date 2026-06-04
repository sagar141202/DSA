# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given the following board:
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
and the word "ABCCED", the function should return true because the word can be found in the grid.

## Approach
The algorithm uses a depth-first search (DFS) approach to explore all possible paths in the grid. It checks if the current character in the word matches the character in the grid, and if so, it continues to the next character. The search is performed in all four directions (up, down, left, right) from each cell.

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
        int rows = board.size();
        int cols = board[0].size();
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, i, j, word, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    
    bool dfs(vector<vector<char>>& board, int i, int j, string word, int k) {
        if (k == word.size()) {
            return true;
        }
        
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || word[k] != board[i][j]) {
            return false;
        }
        
        char temp = board[i][j];
        board[i][j] = '#';
        
        bool found = dfs(board, i + 1, j, word, k + 1) ||
                      dfs(board, i - 1, j, word, k + 1) ||
                      dfs(board, i, j + 1, word, k + 1) ||
                      dfs(board, i, j - 1, word, k + 1);
        
        board[i][j] = temp;
        
        return found;
    }
};
```

## Test Cases
```
Input: board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], word = "ABCCED"
Output: true

Input: board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], word = "SEE"
Output: true

Input: board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], word = "ABCB"
Output: false
```

## Key Takeaways
- Use DFS to explore all possible paths in the grid.
- Keep track of visited cells to avoid revisiting them.
- Restore the original state of the grid after each DFS call.