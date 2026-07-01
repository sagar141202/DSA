# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by filling all 'O's connected to the border of the board with 'X', then flipping all remaining 'O's to 'X' and all 'X's back to 'O'. The board is modified in-place. The input board is represented as a vector of vectors of characters, where each character is either 'X' or 'O'. The output is the modified board.

## Approach
The algorithm uses a depth-first search (DFS) to mark all 'O' regions connected to the border. It then iterates over the board to capture surrounded regions and flip the remaining 'O's and 'X's.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty()) return;
    int m = board.size();
    int n = board[0].size();
    
    // Mark all 'O' regions connected to the border
    for (int i = 0; i < m; i++) {
        if (board[i][0] == 'O') dfs(board, i, 0);
        if (board[i][n-1] == 'O') dfs(board, i, n-1);
    }
    for (int j = 0; j < n; j++) {
        if (board[0][j] == 'O') dfs(board, 0, j);
        if (board[m-1][j] == 'O') dfs(board, m-1, j);
    }
    
    // Capture surrounded regions and flip the remaining 'O's and 'X's
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 'O') board[i][j] = 'X';
            else if (board[i][j] == '#') board[i][j] = 'O';
        }
    }
}

void dfs(vector<vector<char>>& board, int i, int j) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != 'O') return;
    board[i][j] = '#';
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
- Use DFS to mark all 'O' regions connected to the border.
- Capture surrounded regions by flipping all 'O's to 'X' and all 'X's back to 'O' after marking the connected regions.
- The algorithm has a time complexity of O(m*n) where m and n are the dimensions of the board.