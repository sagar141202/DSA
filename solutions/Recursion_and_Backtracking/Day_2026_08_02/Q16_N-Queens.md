# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the field of computer science, where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board where the queens are placed safely. For example, given a 4x4 chessboard, the output should be all possible configurations where 4 queens can be placed without attacking each other.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start by placing the first queen in the first row, then recursively try to place the remaining queens in the subsequent rows. If a queen cannot be placed in a row without being attacked, we backtrack and try a different position for the previous queen.

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
- The time complexity of the solution is O(N!) due to the recursive nature of the algorithm.
- The space complexity is O(N) as we need to store the board and the result.