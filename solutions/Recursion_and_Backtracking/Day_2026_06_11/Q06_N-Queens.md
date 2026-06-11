# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the field of computer science, where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board that satisfy the condition. The input is an integer N, representing the size of the chessboard, and the output is a list of all possible configurations.

## Approach
The solution uses a recursive backtracking approach to try all possible placements of queens on the board. It starts by placing the first queen in the first row, then recursively tries to place the remaining queens in the subsequent rows. If a placement is not valid, it backtracks and tries an alternative placement.

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
- The N-Queens problem can be solved using a recursive backtracking approach.
- The time complexity of the solution is O(N!), where N is the size of the chessboard, due to the recursive nature of the algorithm.
- The space complexity is O(N), where N is the size of the chessboard, due to the storage required for the board and the recursion stack.