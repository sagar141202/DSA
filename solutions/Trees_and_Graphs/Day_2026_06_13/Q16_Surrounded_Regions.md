# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' nodes on the border of the board are connected to it. For example, if we have the following board:
```
X X X X
X O O X
X X O X
X O X X
```
After capture, it should become:
```
X X X X
X X X X
X X X X
X O X X
```
The input will be a 2D vector of characters, and the output should be the modified 2D vector.

## Approach
We can solve this problem by first identifying all 'O' regions connected to the border of the board, marking them as 'N' (not captured), and then flipping all remaining 'O' regions to 'X' and 'N' regions back to 'O'. This approach ensures that only surrounded 'O' regions are captured.

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
        
        // Mark all 'O' regions connected to the border as 'N'
        for (int i = 0; i < m; ++i) {
            dfs(board, i, 0);
            dfs(board, i, n - 1);
        }
        for (int j = 0; j < n; ++j) {
            dfs(board, 0, j);
            dfs(board, m - 1, j);
        }
        
        // Capture surrounded 'O' regions and convert 'N' back to 'O'
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == 'N') {
                    board[i][j] = 'O';
                }
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
- Identify all 'O' regions connected to the border of the board to avoid capturing them.
- Use a depth-first search (DFS) to mark all connected 'O' regions.
- Capture surrounded 'O' regions by flipping them to 'X' and convert marked 'N' regions back to 'O'.