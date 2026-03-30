# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem requires finding all possible configurations of the board where N queens can be placed safely. The input is an integer N, representing the size of the chessboard, and the output is a list of all possible configurations.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start by placing the first queen in the first row and then recursively try to place the remaining queens in the subsequent rows. If a queen cannot be placed in a row without being attacked, we backtrack and try a different position for the previous queen.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<string> board(n, string(n, '.'));
        solve(n, 0, board, result);
        return result;
    }

    void solve(int n, int row, vector<string>& board, vector<vector<string>>& result) {
        if (row == n) {
            result.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isValid(n, row, col, board)) {
                board[row][col] = 'Q';
                solve(n, row + 1, board, result);
                board[row][col] = '.';
            }
        }
    }

    bool isValid(int n, int row, int col, vector<string>& board) {
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
            if (col - (row - i) >= 0 && board[i][col - (row - i)] == 'Q') return false;
            if (col + (row - i) < n && board[i][col + (row - i)] == 'Q') return false;
        }
        return true;
    }
};
```

## Test Cases
```
Input: 4
Output: [
  [".Q..", "...Q", "Q...", "..Q."],
  ["..Q.", "Q...", "...Q", ".Q.."]
]
```

## Key Takeaways
- The N-Queens problem is a classic example of a backtracking problem, where we need to try all possible configurations and backtrack when a configuration is not valid.
- The time complexity of the solution is O(N!), where N is the size of the chessboard, because we are trying all possible configurations.
- The space complexity of the solution is O(N), where N is the size of the chessboard, because we are storing the current configuration of the board.