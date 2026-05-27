# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' nodes on the border of the region are connected to an 'O' node on the border of the board. If a cell is on the border of the board and it's an 'O', then all 'O' cells connected to it are not surrounded. The input is a 2D array of characters, and the output is the modified 2D array.

## Approach
We will use Depth-First Search (DFS) to identify the 'O' regions connected to the border of the board and mark them as 'N' (not surrounded). Then, we will iterate through the board and capture the surrounded 'O' regions by flipping them to 'X', and flip the 'N' nodes back to 'O'.

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
        if (board.empty() || board[0].empty()) return;
        
        int m = board.size();
        int n = board[0].size();
        
        // Mark 'O' regions connected to the border as 'N'
        for (int i = 0; i < m; i++) {
            dfs(board, i, 0);
            dfs(board, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            dfs(board, 0, j);
            dfs(board, m - 1, j);
        }
        
        // Capture surrounded 'O' regions and flip 'N' nodes back to 'O'
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
- Use DFS to identify 'O' regions connected to the border of the board.
- Mark 'O' regions connected to the border as 'N' to differentiate them from surrounded 'O' regions.
- Capture surrounded 'O' regions by flipping them to 'X', and flip 'N' nodes back to 'O'.