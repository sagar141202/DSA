# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' nodes on the border of the region are connected to an 'O' node on the border of the board. If a region is surrounded, all 'O' nodes in that region are flipped to 'X'. Otherwise, the 'O' nodes in that region remain the same.

## Approach
The algorithm involves using a depth-first search (DFS) to mark all 'O' regions connected to the border as not captured. Then, it iterates over the board to capture the surrounded regions by flipping 'O' to 'X' and vice versa.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty()) return;
    int rows = board.size();
    int cols = board[0].size();
    
    // mark all 'O' regions connected to the border as not captured
    for (int i = 0; i < rows; i++) {
        if (board[i][0] == 'O') {
            dfs(board, i, 0);
        }
        if (board[i][cols - 1] == 'O') {
            dfs(board, i, cols - 1);
        }
    }
    for (int j = 0; j < cols; j++) {
        if (board[0][j] == 'O') {
            dfs(board, 0, j);
        }
        if (board[rows - 1][j] == 'O') {
            dfs(board, rows - 1, j);
        }
    }
    
    // capture the surrounded regions
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (board[i][j] == 'O') {
                board[i][j] = 'X';
            } else if (board[i][j] == '#') {
                board[i][j] = 'O';
            }
        }
    }
}

void dfs(vector<vector<char>>& board, int i, int j) {
    if (i < 0 || j < 0 || i >= board.size() || j >= board[0].size() || board[i][j] != 'O') {
        return;
    }
    board[i][j] = '#'; // mark as not captured
    dfs(board, i - 1, j);
    dfs(board, i + 1, j);
    dfs(board, i, j - 1);
    dfs(board, i, j + 1);
}
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
- Identify the border 'O' nodes and mark the connected 'O' regions as not captured.
- Perform a depth-first search to mark the regions.
- Capture the surrounded regions by flipping 'O' to 'X' and vice versa.