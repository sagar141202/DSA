# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the field of computer science, where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board that satisfy the condition. For example, for a 4x4 board, there are two possible configurations.

## Approach
The approach to solve this problem is to use recursion and backtracking, where we try to place a queen in each column and check if the placement is safe. If it is safe, we recursively try to place the next queen. If it is not safe, we backtrack and try a different placement.

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
- Use recursion and backtracking to try all possible placements of queens.
- Check if a placement is safe by verifying that there are no queens in the same column or diagonals.
- Use a helper function to check if a placement is valid, and another to recursively try all possible placements.