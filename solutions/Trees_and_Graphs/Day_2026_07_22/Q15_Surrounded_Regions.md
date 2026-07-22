# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' nodes on the border of the region are connected to the border of the board. For example, if we have the following board:
```
X X X X
X O O X
X X O X
X O X X
```
After capturing the surrounded regions, the board should look like this:
```
X X X X
X X X X
X X X X
X O X X
```
The input is a 2D vector of characters, and the output is the modified board.

## Approach
The algorithm uses depth-first search (DFS) to identify the 'O' regions connected to the border of the board. It first marks these regions as 'N' (not surrounded), then flips all 'O's to 'X' and all 'N's back to 'O'.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty() || board[0].empty()) return;
    
    int rows = board.size();
    int cols = board[0].size();
    
    // Mark 'O' regions connected to the border as 'N'
    for (int i = 0; i < rows; i++) {
        if (board[i][0] == 'O') dfs(board, i, 0);
        if (board[i][cols - 1] == 'O') dfs(board, i, cols - 1);
    }
    for (int j = 0; j < cols; j++) {
        if (board[0][j] == 'O') dfs(board, 0, j);
        if (board[rows - 1][j] == 'O') dfs(board, rows - 1, j);
    }
    
    // Flip 'O' to 'X' and 'N' to 'O'
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
- Identify 'O' regions connected to the border of the board using DFS.
- Mark these regions as 'N' to distinguish them from surrounded 'O' regions.
- Flip all 'O's to 'X' and all 'N's back to 'O' to capture the surrounded regions.