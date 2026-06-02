# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' characters in that region are connected to the border of the board. The input is a 2D vector of characters, and the output should be the modified board after capturing all surrounded regions. For example, if the input is `[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]`, the output should be `[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`.

## Approach
The algorithm involves using depth-first search (DFS) to mark all the 'O' regions connected to the border. Then, it iterates through the board to capture the surrounded regions by flipping 'O' to 'X' and vice versa for the marked 'O' regions.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty() || board[0].empty()) return;
        
        int rows = board.size();
        int cols = board[0].size();
        
        // Mark all 'O' regions connected to the border
        for (int i = 0; i < rows; i++) {
            dfs(board, i, 0);
            dfs(board, i, cols - 1);
        }
        for (int j = 0; j < cols; j++) {
            dfs(board, 0, j);
            dfs(board, rows - 1, j);
        }
        
        // Capture surrounded regions and flip back marked 'O' regions
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
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
};
```

## Test Cases
```
Input: [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
```

## Key Takeaways
- Use DFS to mark all 'O' regions connected to the border.
- Capture surrounded regions by flipping 'O' to 'X' and vice versa for the marked 'O' regions.
- The time complexity is O(M*N) where M and N are the number of rows and columns in the board, respectively.