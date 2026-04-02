# Surrounded Regions

## Problem Statement
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'. A region is captured by flipping all 'O's in that region to 'X'. The board is surrounded by 'X' from the start, so any 'O' connected to the border of the board is not captured. For example, if we have the following board:
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
The input is a 2D vector of characters, where each character is either 'X' or 'O'. The function should modify the input in-place.

## Approach
The algorithm uses depth-first search (DFS) to identify the 'O' regions connected to the border. It first marks these regions with a temporary character, then flips all unmarked 'O' regions to 'X', and finally flips the marked regions back to 'O'.

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
    
    // Mark 'O' regions connected to the border
    for (int i = 0; i < rows; i++) {
        if (board[i][0] == 'O') {
            dfs(board, i, 0, 'O', '#');
        }
        if (board[i][cols - 1] == 'O') {
            dfs(board, i, cols - 1, 'O', '#');
        }
    }
    for (int j = 0; j < cols; j++) {
        if (board[0][j] == 'O') {
            dfs(board, 0, j, 'O', '#');
        }
        if (board[rows - 1][j] == 'O') {
            dfs(board, rows - 1, j, 'O', '#');
        }
    }
    
    // Flip unmarked 'O' regions to 'X' and marked regions back to 'O'
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

void dfs(vector<vector<char>>& board, int i, int j, char oldChar, char newChar) {
    int rows = board.size();
    int cols = board[0].size();
    if (i < 0 || i >= rows || j < 0 || j >= cols || board[i][j] != oldChar) {
        return;
    }
    board[i][j] = newChar;
    dfs(board, i - 1, j, oldChar, newChar);
    dfs(board, i + 1, j, oldChar, newChar);
    dfs(board, i, j - 1, oldChar, newChar);
    dfs(board, i, j + 1, oldChar, newChar);
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
- Use DFS to mark 'O' regions connected to the border.
- Flip unmarked 'O' regions to 'X' and marked regions back to 'O' in a second pass.
- The algorithm has a time complexity of O(M*N) and a space complexity of O(M*N) due to the recursive call stack.