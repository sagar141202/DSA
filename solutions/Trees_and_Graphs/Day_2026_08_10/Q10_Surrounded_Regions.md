# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by filling all 'O's in that region with 'X'. The region is surrounded only if all 'O's in that region are connected to the border of the board. For example, if we have the following board:
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
The input is a 2D vector of characters, where each character is either 'X' or 'O'. The output is the modified 2D vector.

## Approach
The approach to solve this problem is to start from the border of the board and mark all connected 'O' regions as 'N' (not surrounded). Then, iterate over the entire board and capture all 'O' regions by replacing them with 'X'. Finally, replace all 'N' with 'O' to get the final result.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty()) return;
    int m = board.size();
    int n = board[0].size();
    
    // Mark all 'O' regions connected to the border as 'N'
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
    
    // Capture all 'O' regions and replace 'N' with 'O'
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
    int m = board.size();
    int n = board[0].size();
    if (i < 0 || i >= m || j < 0 || j >= n || board[i][j] != 'O') {
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
- The key to solving this problem is to first identify all 'O' regions connected to the border and mark them as 'N'.
- Then, capture all 'O' regions by replacing them with 'X'.
- Finally, replace all 'N' with 'O' to get the final result.
- The time complexity of this solution is O(m*n), where m and n are the dimensions of the board.