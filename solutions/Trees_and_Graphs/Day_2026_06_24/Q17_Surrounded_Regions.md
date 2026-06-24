# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' nodes on the border of the region are connected to the border of the board. For example, if we have the following board:
```
X X X X
X O O X
X X O X
X O X X
```
After running the function, the board should be:
```
X X X X
X X X X
X X X X
X O X X
```
The constraints are: the input board is a 2D vector of characters, where each character is either 'X' or 'O'. The board has at least one row and one column.

## Approach
The approach involves using depth-first search (DFS) to mark all 'O' regions connected to the border of the board. Then, iterate through the board to capture all 'O' regions that are not marked. The algorithm works by first identifying the 'O' regions connected to the border, then flipping all other 'O' regions to 'X'.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty() || board[0].empty()) return;
    
    int m = board.size();
    int n = board[0].size();
    
    // Mark all 'O' regions connected to the border
    for (int i = 0; i < m; i++) {
        if (board[i][0] == 'O') {
            dfs(board, i, 0);
        }
        if (board[i][n - 1] == 'O') {
            dfs(board, i, n - 1);
        }
    }
    for (int j = 0; j < n; j++) {
        if (board[0][j] == 'O') {
            dfs(board, 0, j);
        }
        if (board[m - 1][j] == 'O') {
            dfs(board, m - 1, j);
        }
    }
    
    // Capture all 'O' regions that are not marked
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 'O') {
                board[i][j] = 'X';
            } else if (board[i][j] == '#') {
                board[i][j] = 'O';
            }
        }
    }
}

void dfs(vector<vector<char>>& board, int i, int j) {
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != 'O') {
        return;
    }
    board[i][j] = '#';
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
- Use DFS to mark all 'O' regions connected to the border of the board.
- Iterate through the board to capture all 'O' regions that are not marked.
- Use a temporary marker ('#') to mark the 'O' regions connected to the border, and then replace it with 'O' after capturing all other 'O' regions.