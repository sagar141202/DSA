# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board where N queens can be placed safely. The constraints are: 1 <= N <= 9, and the board is a square (i.e., it has the same number of rows and columns). For example, if N = 4, the output should be all possible configurations of a 4x4 chessboard where 4 queens can be placed without attacking each other.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will try to place a queen in each column of the board, and for each placement, we will recursively try to place the remaining queens. If a placement is not safe (i.e., it attacks another queen), we will backtrack and try a different placement.

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
        vector<int> board(n, -1);
        solve(n, 0, board, result);
        return result;
    }

    void solve(int n, int row, vector<int>& board, vector<vector<string>>& result) {
        if (row == n) {
            // Convert the board to a string representation
            vector<string> solution(n, string(n, '.'));
            for (int i = 0; i < n; i++) {
                solution[i][board[i]] = 'Q';
            }
            result.push_back(solution);
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(n, row, col, board)) {
                board[row] = col;
                solve(n, row + 1, board, result);
            }
        }
    }

    bool isSafe(int n, int row, int col, vector<int>& board) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || 
                board[i] - i == col - row || 
                board[i] + i == col + row) {
                return false;
            }
        }
        return true;
    }
};
```

## Test Cases
```
Input: n = 4
Output: [
  [".Q..", "...Q", "Q...", "..Q."],
  ["..Q.", "Q...", "...Q", ".Q.."]
]
```

## Key Takeaways
- Recursion and backtracking are useful techniques for solving problems that involve exploring a large solution space.
- The N-Queens problem is a classic example of a problem that can be solved using recursion and backtracking.
- The time complexity of the solution is O(N!) because there are N! possible configurations of the board.