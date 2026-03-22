# Word Search

## Problem Statement
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once. For example, given a 2D board containing the letters [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ] and the word "ABCCED", the function should return True, because the word can be found in the grid.

## Approach
The algorithm uses depth-first search (DFS) to traverse the grid and check if the word can be formed. It starts from each cell in the grid and explores all possible paths. The search is terminated when the entire word is found or when there are no more adjacent cells to explore.

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
        int rows = board.size();
        int cols = board[0].size();
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
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
Input: board = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], word = "ABCCED"
Output: True
Input: board = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], word = "SEE"
Output: True
Input: board = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ], word = "ABCB"
Output: False
```

## Key Takeaways
- Use DFS to explore all possible paths in the grid.
- Mark visited cells to avoid revisiting them.
- Restore the original state of the grid after exploring each path.