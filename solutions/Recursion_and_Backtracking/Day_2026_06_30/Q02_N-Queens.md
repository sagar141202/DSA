# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in computer science where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board where the queens do not attack each other. The input is an integer N, representing the size of the chessboard, and the output is a list of all possible configurations.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start by placing the first queen in the first row and then recursively try to place the remaining queens in the subsequent rows. If a queen cannot be placed in a row without being attacked, we backtrack and try a different position in the previous row.

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
- The N-Queens problem is a classic example of a problem that can be solved using recursion and backtracking.
- The time complexity of the solution is O(N!) because there are N! possible configurations of the board.
- The space complexity of the solution is O(N) because we need to store the current configuration of the board.