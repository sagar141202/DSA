# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by filling all 'O's connected to the border of the board with 'X'. The remaining 'O's are the ones that are not surrounded by 'X'. For example, given the board:
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
The constraints are: the board is a 2D vector of characters, and it is not empty.

## Approach
The algorithm uses depth-first search (DFS) to mark 'O' regions connected to the border. It then iterates over the board, capturing surrounded 'O' regions and keeping the border-connected 'O' regions.

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

    // Mark 'O' regions connected to the border
    for (int i = 0; i < m; ++i) {
        if (board[i][0] == 'O') dfs(board, i, 0);
        if (board[i][n-1] == 'O') dfs(board, i, n-1);
    }
    for (int j = 0; j < n; ++j) {
        if (board[0][j] == 'O') dfs(board, 0, j);
        if (board[m-1][j] == 'O') dfs(board, m-1, j);
    }

    // Capture surrounded 'O' regions and keep border-connected 'O' regions
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (board[i][j] == 'O') board[i][j] = 'X';
            else if (board[i][j] == '#') board[i][j] = 'O';
        }
    }
}

void dfs(vector<vector<char>>& board, int i, int j) {
    int m = board.size();
    int n = board[0].size();
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != 'O') return;
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
- Use DFS to mark 'O' regions connected to the border.
- Use a temporary marker '#' to keep track of visited 'O' cells.
- Capture surrounded 'O' regions by replacing them with 'X', and keep border-connected 'O' regions by replacing '#' with 'O'.