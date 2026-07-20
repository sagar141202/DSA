# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The board is surrounded by 'X' from the outside, so any 'O' connected to the border of the board is not surrounded. The input board will be a 2D array of characters, and the output will be the modified board after capturing all surrounded regions. For example, if the input is 
```
X X X X
X O O X
X X O X
X O X X
```
the output should be
```
X X X X
X X X X
X X X X
X O X X
```
The constraints are that the input board will have at most 100 rows and 100 columns, and the board will only contain 'X' and 'O'.

## Approach
The algorithm will start from the border of the board and mark all connected 'O' regions as 'N' (not surrounded). Then, it will iterate over the board and capture all 'O' regions by flipping them to 'X', and flip back the 'N' regions to 'O'.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty() || board[0].empty()) return;
    int m = board.size(), n = board[0].size();
    
    // mark all connected 'O' regions from the border as 'N'
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
    
    // capture all 'O' regions and flip back 'N' regions
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
    int m = board.size(), n = board[0].size();
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != 'O') return;
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
X X X X
X O O X
X X O X
X O X X
Output: 
X X X X
X X X X
X X X X
X O X X
```

## Key Takeaways
- Start from the border of the board to mark all connected 'O' regions as 'N'.
- Use DFS to traverse all connected 'O' regions from the border.
- Capture all 'O' regions by flipping them to 'X', and flip back the 'N' regions to 'O'.