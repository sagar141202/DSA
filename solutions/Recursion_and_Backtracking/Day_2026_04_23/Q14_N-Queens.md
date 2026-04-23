# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem requires finding all possible configurations of the board where N queens are placed safely. The input is an integer N, representing the size of the chessboard, and the output is a list of all possible configurations.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start by placing the first queen in the first column and then recursively try to place the remaining queens in the subsequent columns. If a queen cannot be placed in any row of the current column, we backtrack and try a different position for the previous queen.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<string> board(n, string(n, '.'));
        solve(result, board, 0);
        return result;
    }

    void solve(vector<vector<string>>& result, vector<string>& board, int row) {
        if (row == board.size()) {
            result.push_back(board);
            return;
        }
        for (int col = 0; col < board.size(); col++) {
            if (isValid(board, row, col)) {
                board[row][col] = 'Q';
                solve(result, board, row + 1);
                board[row][col] = '.';
            }
        }
    }

    bool isValid(vector<string>& board, int row, int col) {
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < board.size(); j++) {
                if (board[i][j] == 'Q' && (j == col || abs(j - col) == row - i)) {
                    return false;
                }
            }
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
- The N-Queens problem is a classic example of a problem that can be solved using recursion and backtracking.
- The time complexity of the solution is O(N!) because there are N! possible configurations of the board.
- The space complexity of the solution is O(N) because we need to store the current configuration of the board.