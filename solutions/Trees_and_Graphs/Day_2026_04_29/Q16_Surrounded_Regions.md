# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' cells in that region are connected to the border of the board. For example, if we have the following board:
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
The constraints are: the input board is a 2D vector of characters, the number of rows and columns in the board are in the range [1, 200], and the board only contains 'X' and 'O'.

## Approach
The algorithm involves using a depth-first search (DFS) to identify the 'O' regions connected to the border of the board and marking them as 'N' (not captured). Then, it iterates over the board to capture the surrounded 'O' regions by flipping them to 'X' and restore the 'N' regions to 'O'.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty() || board[0].empty()) return;
        int rows = board.size();
        int cols = board[0].size();
        
        // Mark 'O' regions connected to the border as 'N'
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
        
        // Capture surrounded 'O' regions and restore 'N' regions
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
};

int main() {
    Solution solution;
    vector<vector<char>> board = {
        {'X', 'X', 'X', 'X'},
        {'X', 'O', 'O', 'X'},
        {'X', 'X', 'O', 'X'},
        {'X', 'O', 'X', 'X'}
    };
    solution.solve(board);
    for (auto& row : board) {
        for (char cell : row) {
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
- Use DFS to mark 'O' regions connected to the border as 'N' to avoid capturing them.
- Iterate over the board to capture surrounded 'O' regions by flipping them to 'X' and restore the 'N' regions to 'O'.
- The time complexity is O(M*N) where M and N are the number of rows and columns in the board, respectively.