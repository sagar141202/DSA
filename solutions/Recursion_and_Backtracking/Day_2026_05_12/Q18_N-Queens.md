# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem requires finding all possible configurations of the board where N queens can be placed safely. The input is an integer N, representing the size of the chessboard, and the output is a list of all possible board configurations.

## Approach
The problem can be solved using recursion and backtracking, by trying to place a queen in each column and checking if the placement is safe. If the placement is safe, the algorithm moves to the next column; otherwise, it backtracks and tries a different placement.

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
        
        // Check the column
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') {
                return false;
            }
        }
        
        // Check the upper-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') {
                return false;
            }
        }
        
        // Check the upper-right diagonal
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
    int n = 4;
    vector<vector<string>> result = solution.solveNQueens(n);
    
    for (int i = 0; i < result.size(); i++) {
        cout << "Configuration " << i + 1 << ":" << endl;
        for (int j = 0; j < n; j++) {
            cout << result[i][j] << endl;
        }
        cout << endl;
    }
    
    return 0;
}
```

## Test Cases
```
Input: n = 4
Output: 
Configuration 1:
. Q . .
. . . Q
Q . . .
. . Q .
 
Configuration 2:
. . Q .
Q . . .
. . . Q
. Q . .
```

## Key Takeaways
- The N-Queens problem can be solved using recursion and backtracking.
- The algorithm tries to place a queen in each column and checks if the placement is safe.
- The time complexity of the algorithm is O(N!), where N is the size of the chessboard.