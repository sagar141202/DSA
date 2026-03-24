# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by filling all 'O's connected to the border of the board with 'X', then flipping all remaining 'O's to 'X' and all 'X's back to 'O'. The board is modified in-place. The input board is an m x n matrix, where m and n are the number of rows and columns, respectively. The constraints are 1 <= m, n <= 200, board[i][j] is 'X' or 'O'.

## Approach
The algorithm involves identifying the 'O' regions connected to the border of the board and marking them as temporary 'N' (not captured). Then, it captures all the remaining 'O' regions by filling them with 'X', and finally flips the 'N' regions back to 'O' and the 'X' regions (previously 'O') back to 'O'. This approach ensures that only the 'O' regions surrounded by 'X' are captured.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty() || board[0].empty()) return;
        
        int m = board.size();
        int n = board[0].size();
        
        // Mark 'O' regions connected to the border as 'N'
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') dfs(board, i, 0);
            if (board[i][n - 1] == 'O') dfs(board, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') dfs(board, 0, j);
            if (board[m - 1][j] == 'O') dfs(board, m - 1, j);
        }
        
        // Capture 'O' regions and flip 'N' back to 'O'
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                else if (board[i][j] == 'N') board[i][j] = 'O';
            }
        }
    }
    
    void dfs(vector<vector<char>>& board, int i, int j) {
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != 'O') return;
        board[i][j] = 'N';
        dfs(board, i - 1, j);
        dfs(board, i + 1, j);
        dfs(board, i, j - 1);
        dfs(board, i, j + 1);
    }
};

```

## Test Cases
```
Input: 
[
  ['X','X','X','X'],
  ['X','O','O','X'],
  ['X','X','O','X'],
  ['X','O','X','X']
]
Output: 
[
  ['X','X','X','X'],
  ['X','X','X','X'],
  ['X','X','X','X'],
  ['X','O','X','X']
]
```

## Key Takeaways
- Identify the 'O' regions connected to the border of the board.
- Use DFS to mark these regions as temporary 'N'.
- Capture the remaining 'O' regions by filling them with 'X'.
- Flip the 'N' regions back to 'O' and the 'X' regions (previously 'O') back to 'O'.