# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The board is surrounded by 'X' from the start, so any 'O' connected to the border of the board is not captured. For example, given the following board:
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
The constraints are: the input is a 2D vector of characters, the number of rows and columns in the board will be in the range [1, 200], and the board will only contain 'X' and 'O'.

## Approach
The approach to this problem is to start from the border of the board and mark all the 'O' regions connected to the border. Then, we can iterate over the board and flip all the unmarked 'O' regions to 'X' and mark all the marked 'O' regions back to 'O'.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty() || board[0].empty()) return;
    
    int M = board.size();
    int N = board[0].size();
    
    // mark all 'O' regions connected to the border
    for (int i = 0; i < M; i++) {
        if (board[i][0] == 'O') {
            dfs(board, i, 0);
        }
        if (board[i][N-1] == 'O') {
            dfs(board, i, N-1);
        }
    }
    for (int j = 0; j < N; j++) {
        if (board[0][j] == 'O') {
            dfs(board, 0, j);
        }
        if (board[M-1][j] == 'O') {
            dfs(board, M-1, j);
        }
    }
    
    // flip all the unmarked 'O' regions to 'X' and mark all the marked 'O' regions back to 'O'
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i][j] == 'O') {
                board[i][j] = 'X';
            } else if (board[i][j] == '#') {
                board[i][j] = 'O';
            }
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
- Use DFS to mark all the 'O' regions connected to the border.
- Flip all the unmarked 'O' regions to 'X' and mark all the marked 'O' regions back to 'O' after DFS.
- The time complexity is O(M*N) where M is the number of rows and N is the number of columns in the board.