# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O', capture all regions of 'O' that are not surrounded by 'X' from the border of the board. A region is captured by filling all 'O's in that region with 'X'. The board is modified in-place.

## Approach
The algorithm uses a depth-first search (DFS) approach to mark all 'O' regions connected to the border as 'N' (not surrounded), and then iterates over the board to capture surrounded 'O' regions and restore 'N' regions to 'O'.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;
        
        int rows = board.size();
        int cols = board[0].size();
        
        // Mark 'O' regions connected to the border as 'N'
        for (int i = 0; i < rows; i++) {
            dfs(board, i, 0);
            dfs(board, i, cols - 1);
        }
        for (int j = 0; j < cols; j++) {
            dfs(board, 0, j);
            dfs(board, rows - 1, j);
        }
        
        // Capture surrounded 'O' regions and restore 'N' regions to 'O'
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
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
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: 
[
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
```

## Key Takeaways
- Use DFS to mark connected components.
- Modify the board in-place to avoid extra space complexity.
- Restore the marked regions after capturing surrounded regions.