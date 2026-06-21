# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem requires finding all possible configurations of the board where N queens are placed safely. The input is an integer N, representing the size of the chessboard, and the output is a list of all possible configurations. For example, for N = 4, there are two possible configurations.

## Approach
The algorithm uses backtracking to try all possible placements of queens on the board, ensuring that each placement is safe from attack by any previously placed queen. The solution iterates through each row and attempts to place a queen in each column, checking for safety after each placement. If a placement is safe, the algorithm recursively tries to place the remaining queens.

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
            for (int j = 0; j < n; j++) {
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
Output: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
```

## Key Takeaways
- Use backtracking to explore all possible configurations of the board.
- Ensure each placement of a queen is safe from attack by any previously placed queen.
- The time complexity of the solution is O(N!) due to the recursive nature of the backtracking algorithm.