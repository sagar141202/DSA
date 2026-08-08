# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The region is surrounded if all 'O' nodes on the border of the region are connected to the border of the board. For example, if we have the following board:
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
The board is modified in-place.

## Approach
The algorithm uses depth-first search (DFS) to mark all 'O' regions connected to the border of the board. Then it iterates over the board to capture the surrounded regions by flipping 'O' to 'X' and vice versa for the marked regions.

## Complexity
- Time: O(M*N)
- Space: O(M*N)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void solve(vector<vector<char>>& board) {
    if (board.empty() || board[0].empty()) return;

    int rows = board.size();
    int cols = board[0].size();

    // Mark all 'O' regions connected to the border
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

    // Capture surrounded regions and revert marked regions
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
    board[i][j] = '#'; // Mark as visited
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
- Use DFS to mark all 'O' regions connected to the border of the board.
- Capture surrounded regions by flipping 'O' to 'X' and vice versa for the marked regions.
- The algorithm has a time complexity of O(M*N) and a space complexity of O(M*N), where M and N are the number of rows and columns in the board, respectively.