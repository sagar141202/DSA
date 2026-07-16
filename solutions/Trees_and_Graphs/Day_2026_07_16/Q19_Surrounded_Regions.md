# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by filling all 'O's connected to the border of the board with 'X', then flipping all 'O's to 'X' and all 'X's to 'O'. The board is modified in-place. The input is a 2D vector of characters, and the output is the modified board. For example, given the following board:
```
X X X X
X O O X
X X O X
X O X X
```
The output should be:
```
X X X X
X X X X
X X X X
X O X X
```
The constraints are that the input board is a 2D vector of characters, where each character is either 'X' or 'O', and the board is not empty.

## Approach
The algorithm uses depth-first search to mark all 'O' regions connected to the border as 'N' (not surrounded), then iterates over the board to flip 'O' to 'X' and 'N' to 'O'. This approach ensures that only surrounded 'O' regions are flipped to 'X'.

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
    
    // mark all 'O' regions connected to the border as 'N'
    for (int i = 0; i < M; i++) {
        if (board[i][0] == 'O') dfs(board, i, 0);
        if (board[i][N-1] == 'O') dfs(board, i, N-1);
    }
    for (int j = 0; j < N; j++) {
        if (board[0][j] == 'O') dfs(board, 0, j);
        if (board[M-1][j] == 'O') dfs(board, M-1, j);
    }
    
    // flip 'O' to 'X' and 'N' to 'O'
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i][j] == 'O') board[i][j] = 'X';
            else if (board[i][j] == 'N') board[i][j] = 'O';
        }
    }
}

void dfs(vector<vector<char>>& board, int i, int j) {
    int M = board.size();
    int N = board[0].size();
    
    if (i < 0 || i >= M || j < 0 || j >= N || board[i][j] != 'O') return;
    
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
- Use depth-first search to mark all 'O' regions connected to the border as 'N'.
- Iterate over the board to flip 'O' to 'X' and 'N' to 'O' in a single pass.
- The time complexity is O(M*N) because we visit each cell at most twice.