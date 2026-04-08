# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'. A region is captured by filling all 'O's in that region with 'X'. The region is surrounded if all 'O' characters are not connected to the border of the board. For example, consider the following board:
```
X X X X
X O O X
X X O X
X O X X
```
After capturing the surrounded regions, the board should look like:
```
X X X X
X X X X
X X X X
X O X X
```
The input is a 2D vector of characters, and the output is the modified 2D vector.

## Approach
The approach is to first identify all 'O' regions connected to the border and mark them as 'N' (not captured). Then, iterate over the board to capture all 'O' regions by filling them with 'X', and finally convert all 'N' back to 'O'.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty() || board[0].empty()) return;
    
    int m = board.size();
    int n = board[0].size();
    
    // Mark all 'O' regions connected to the border as 'N'
    for (int i = 0; i < m; i++) {
        if (board[i][0] == 'O') {
            dfs(board, i, 0);
        }
        if (board[i][n-1] == 'O') {
            dfs(board, i, n-1);
        }
    }
    for (int j = 0; j < n; j++) {
        if (board[0][j] == 'O') {
            dfs(board, 0, j);
        }
        if (board[m-1][j] == 'O') {
            dfs(board, m-1, j);
        }
    }
    
    // Capture all 'O' regions and convert 'N' back to 'O'
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 'O') {
                board[i][j] = 'X';
            } else if (board[i][j] == 'N') {
                board[i][j] = 'O';
            }
        }
    }
}

void dfs(vector<vector<char>>& board, int i, int j) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != 'O') {
        return;
    }
    board[i][j] = 'N';
    dfs(board, i-1, j);
    dfs(board, i+1, j);
    dfs(board, i, j-1);
    dfs(board, i, j+1);
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
- Identify the regions connected to the border to avoid capturing them.
- Use a depth-first search (DFS) to mark all connected 'O' regions as 'N'.
- Iterate over the board to capture all 'O' regions and convert 'N' back to 'O'.