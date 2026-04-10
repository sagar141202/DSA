# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the field of computer science, where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem statement requires finding all possible configurations of the board where N queens can be placed safely. For example, for N = 4, there are two possible configurations: 
[
    [".Q..", "...Q", "Q...", "..Q."],
    ["..Q.", "Q...", "...Q", ".Q.."]
]
The constraints are: 
- The input is an integer N, representing the size of the chessboard.
- The output should be a list of all possible configurations, where each configuration is a list of strings representing the rows of the chessboard.

## Approach
The approach to solve this problem is to use backtracking, where we try to place a queen in each column of the current row and recursively check if the placement is safe. If it's safe, we move to the next row; otherwise, we backtrack and try a different placement.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <vector>
#include <string>
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
            if (isSafe(board, row, col)) {
                board[row][col] = 'Q';
                backtrack(result, board, row + 1);
                board[row][col] = '.';
            }
        }
    }

    bool isSafe(vector<string>& board, int row, int col) {
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
- The N-Queens problem can be solved using backtracking, which is a technique for solving problems by recursively exploring all possible solutions.
- The time complexity of the solution is O(N!), where N is the number of queens, because in the worst case, we have to try all possible placements of the queens.
- The space complexity of the solution is O(N), where N is the number of queens, because we need to store the current state of the board.