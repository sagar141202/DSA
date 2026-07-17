# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the field of computer science, where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem statement requires finding all possible configurations of the board where N queens can be placed safely. For example, for a 4x4 board, there are two possible configurations: 
{
{".Q..", "...Q", "Q...", "..Q."},
{".Q..", "..Q.", "Q...", "...Q"}
}
The constraints are: 1 <= N <= 9, and the board is a square (i.e., it has the same number of rows and columns).

## Approach
The approach to solve this problem involves using recursion and backtracking to try all possible placements of the queens on the board. We iterate through each row and try to place a queen in each column, checking if the placement is safe. If it is safe, we recursively try to place the remaining queens.

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
                if (board[i][j] == 'Q' && (j == col || abs(j - col) == abs(i - row))) {
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
- The time complexity of the solution is O(N!) because in the worst case, we have to try all possible placements of the queens.
- The space complexity is O(N) because we need to store the current state of the board.