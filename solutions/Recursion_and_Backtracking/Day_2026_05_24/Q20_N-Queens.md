# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in computer science where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board that satisfy this condition. For example, given a 4x4 chessboard, the solution should return all possible ways to place 4 queens on the board such that no two queens attack each other.

## Approach
The algorithm uses backtracking to try all possible placements of queens on the board. It starts by placing the first queen in the first column, and then recursively tries to place the remaining queens in the next columns. If a queen cannot be placed in a column without being attacked, the algorithm backtracks and tries a different placement for the previous queen.

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
        
        // Check column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') {
                return false;
            }
        }
        
        // Check upper-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        // Check upper-right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        return true;
    }
};

int main() {
    Solution solution;
    vector<vector<string>> result = solution.solveNQueens(4);
    for (auto& board : result) {
        for (auto& row : board) {
            cout << row << endl;
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: 4
Output: 
. Q . .
. . . Q
Q . . .
. . Q .

. . Q .
Q . . .
. . . Q
. Q . .
```

## Key Takeaways
- The N-Queens problem is a classic example of a backtracking problem, where the algorithm tries all possible solutions and backtracks when a dead end is reached.
- The use of a recursive function to try all possible placements of queens makes the code more efficient and easier to understand.
- The `isValid` function is used to check if a queen can be placed at a given position on the board without being attacked by any other queen.