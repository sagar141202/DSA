# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. Given an integer N, return all possible configurations of the board where N queens can be placed without any attacks. For example, for N = 4, one possible configuration is:
```
. Q . .
. . . Q
Q . . .
. . Q .
```
The constraints are:
- 1 <= N <= 10
- The board is a square of size NxN
- Each queen can be placed in any empty cell

## Approach
The approach to solve this problem is to use recursion and backtracking. We start by placing the first queen in the first column, then recursively try to place the next queen in the next column. If we cannot place a queen in any row of the current column, we backtrack and try a different row for the previous queen.

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
        solve(board, 0, result);
        return result;
    }
    
    void solve(vector<string>& board, int col, vector<vector<string>>& result) {
        if (col == board.size()) {
            result.push_back(board);
            return;
        }
        
        for (int row = 0; row < board.size(); row++) {
            if (isValid(board, row, col)) {
                board[row][col] = 'Q';
                solve(board, col + 1, result);
                board[row][col] = '.';
            }
        }
    }
    
    bool isValid(vector<string>& board, int row, int col) {
        int n = board.size();
        
        // Check this row on left side
        for (int i = 0; i < col; i++) {
            if (board[row][i] == 'Q') {
                return false;
            }
        }
        
        // Check upper diagonal on left side
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        // Check lower diagonal on left side
        for (int i = row, j = col; j >= 0 && i < n; i++, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        return true;
    }
};

int main() {
    Solution solution;
    int n = 4;
    vector<vector<string>> result = solution.solveNQueens(n);
    for (auto& config : result) {
        for (auto& row : config) {
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
- Recursion and backtracking can be used to solve problems that require exploring all possible configurations.
- The N-Queens problem has a time complexity of O(N!) due to the recursive nature of the solution.
- The space complexity is O(N) for storing the board and the result.