# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the field of computer science and chess. The problem statement is as follows: given an NxN chessboard, place N queens on the board such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The goal is to find all possible configurations of the board where N queens can be placed safely. For example, for a 4x4 board, there are two possible configurations.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start by placing the first queen in the first row, then recursively try to place the remaining queens in the subsequent rows. If a queen cannot be placed in a row without being attacked, we backtrack and try a different position for the previous queen.

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
        solve(board, 0, result);
        return result;
    }

    void solve(vector<string>& board, int row, vector<vector<string>>& result) {
        int n = board.size();
        if (row == n) {
            result.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isValid(board, row, col)) {
                board[row][col] = 'Q';
                solve(board, row + 1, result);
                board[row][col] = '.';
            }
        }
    }

    bool isValid(vector<string>& board, int row, int col) {
        int n = board.size();
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
        }
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') return false;
        }
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') return false;
        }
        return true;
    }
};
```

## Test Cases
```
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```

## Key Takeaways
- Use recursion and backtracking to solve the N-Queens problem.
- The time complexity is O(N!) due to the recursive nature of the solution.
- The space complexity is O(N) for the recursive call stack and the board representation.