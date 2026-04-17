# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' connected to the edge of the board are 'X'. For example, if we have the following board:
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
The input is a 2D vector of characters, and the output is the modified 2D vector.

## Approach
We use a depth-first search (DFS) approach to mark all 'O' regions connected to the edge of the board. We start from the edges and mark all connected 'O' as 'N' (not surrounded). Then we iterate over the board and flip all 'O' to 'X' and all 'N' back to 'O'.

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
    
    // Mark all 'O' regions connected to the edge of the board as 'N'
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
    
    // Flip all 'O' to 'X' and all 'N' back to 'O'
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
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
    for (auto row : board) {
        for (auto cell : row) {
            cout << cell << " ";
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
- Use DFS to mark all 'O' regions connected to the edge of the board as 'N'.
- Iterate over the board to flip all 'O' to 'X' and all 'N' back to 'O'.
- The time complexity is O(M*N) where M is the number of rows and N is the number of columns in the board.