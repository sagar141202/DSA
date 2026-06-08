# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' characters are connected to the border of the board. For example, consider the following board:
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
The input is a 2D vector of characters where 'X' represents an X and 'O' represents an O. The function should modify the input in-place.

## Approach
The approach is to start from the border of the board and perform a depth-first search (DFS) to mark all connected 'O' regions as 'N' (not surrounded). Then, iterate over the board to flip all 'O's to 'X' and all 'N's back to 'O'.

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
    
    // mark all 'O' regions connected to the border as 'N'
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
    
    // flip all 'O's to 'X' and all 'N's back to 'O'
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
    if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != 'O') return;
    
    board[i][j] = 'N';
    dfs(board, i - 1, j);
    dfs(board, i + 1, j);
    dfs(board, i, j - 1);
    dfs(board, i, j + 1);
}

int main() {
    vector<vector<char>> board = {
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'X', 'O', 'X'},
        {'X', 'O', 'X', 'X'}
    };
    
    solve(board);
    
    for (const auto& row : board) {
        for (char c : row) {
            cout << c << " ";
        }
        cout << endl;
    }
    
    return 0;
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
- Use DFS to traverse the board and mark all connected 'O' regions.
- Flip all 'O's to 'X' and all 'N's back to 'O' after DFS.