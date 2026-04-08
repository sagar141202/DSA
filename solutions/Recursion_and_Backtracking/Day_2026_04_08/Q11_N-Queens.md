# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in computer science where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem statement requires finding all possible configurations of the board where the queens do not attack each other. The input is an integer N, representing the size of the chessboard, and the output is a list of all possible configurations.

## Approach
The algorithm uses recursion and backtracking to try all possible placements of the queens on the board. It starts by placing the first queen in the first column, then recursively tries to place the remaining queens in the subsequent columns. If a queen cannot be placed in any row of the current column without being attacked, the algorithm backtracks and tries a different placement for the previous queen.

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
        int n = board.size();
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
- The N-Queens problem can be solved using recursion and backtracking by trying all possible placements of the queens on the board.
- The time complexity of the solution is O(N!) due to the recursive nature of the algorithm.
- The space complexity of the solution is O(N) for storing the current state of the board.