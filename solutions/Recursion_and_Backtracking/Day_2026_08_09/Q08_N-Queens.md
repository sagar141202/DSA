# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board where N queens can be placed safely. The input is an integer N, representing the size of the chessboard, and the output is a list of all possible configurations, where each configuration is represented as a 2D vector of strings, with 'Q' denoting a queen and '.' denoting an empty space. For example, for N = 4, one possible configuration is:
```
. Q . .
. . . Q
Q . . .
. . Q .
```
The constraints are 1 <= N <= 9, and the output should be a list of all possible configurations.

## Approach
The approach to solve this problem is to use backtracking and recursion to try all possible placements of queens on the board. We start by placing the first queen in the first row, and then recursively try to place the remaining queens in the subsequent rows, ensuring that each placement is safe.

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
        backtrack(result, board, 0);
        return result;
    }

    void backtrack(vector<vector<string>>& result, vector<string>& board, int row) {
        if (row == board.size()) {
            result.push_back(board);
            return;
        }
        for (int col = 0; col < board.size(); col++) {
            if (isValid(board, row, col)) {
                board[row][col] = 'Q';
                backtrack(result, board, row + 1);
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
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```

## Key Takeaways
- The N-Queens problem is a classic example of a backtracking problem, where we try all possible placements of queens on the board and backtrack when a placement is not safe.
- The time complexity of the solution is O(N!), where N is the size of the board, because we try all possible placements of queens.
- The space complexity of the solution is O(N), where N is the size of the board, because we need to store the current state of the board.