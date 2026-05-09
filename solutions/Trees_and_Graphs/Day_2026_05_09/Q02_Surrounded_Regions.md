# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' nodes on the border of the region are connected to an 'O' node on the border of the board. If there is no 'O' node on the border of the board, the region is not surrounded. For example, given the following board:
```
X X X X
X O O X
X X O X
X O X X
```
After running a capture operation, the board should be:
```
X X X X
X X X X
X X X X
X O X X
```
The constraints are: the input board is a 2D vector of characters, the number of rows and columns in the board are in the range [1, 200], and the board is not empty.

## Approach
The approach involves using depth-first search (DFS) to identify 'O' regions connected to the border of the board and mark them as not surrounded. Then, we iterate over the board to capture the surrounded 'O' regions by flipping them to 'X' and flip back the marked 'O' regions.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty() || board[0].empty()) return;
    
    int m = board.size();
    int n = board[0].size();
    
    // Mark 'O' regions connected to the border as not surrounded
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
    
    // Capture surrounded 'O' regions and flip back marked 'O' regions
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
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
    board[i][j] = '#'; // Mark as not surrounded
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
- Use DFS to mark 'O' regions connected to the border as not surrounded.
- Capture surrounded 'O' regions and flip back marked 'O' regions in a second pass.
- The time complexity is O(m*n) due to the DFS and the second pass over the board.