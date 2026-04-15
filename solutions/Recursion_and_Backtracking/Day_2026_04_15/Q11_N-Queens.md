# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the field of computer science and chess. The problem statement is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The task is to find all possible configurations of the board where N queens can be placed safely. For example, for a 4x4 board, there are two possible configurations: 
[
    [".Q..", "...Q", "Q...", "..Q."],
    ["..Q.", "Q...", "...Q", ".Q.."]
]
The input is an integer N, representing the size of the chessboard. The output should be a list of all possible configurations, where each configuration is represented as a list of strings, with 'Q' representing a queen and '.' representing an empty space.

## Approach
The approach to solve this problem is to use a recursive backtracking algorithm. The algorithm tries to place a queen in each column of the current row, and checks if the placement is safe. If it is safe, the algorithm recursively tries to place queens in the next row.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <vector>
#include <string>

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
            if (board[i][col] == 'Q') return false;
            if (col - (row - i) >= 0 && board[i][col - (row - i)] == 'Q') return false;
            if (col + (row - i) < board.size() && board[i][col + (row - i)] == 'Q') return false;
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
- The N-Queens problem can be solved using a recursive backtracking algorithm.
- The algorithm tries to place a queen in each column of the current row, and checks if the placement is safe.
- The time complexity of the algorithm is O(N!), where N is the size of the chessboard.