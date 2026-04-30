# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem requires finding all possible configurations of the board where N queens can be placed safely. The constraints are: (1) each queen must be placed in a different row, (2) no two queens can be in the same column, and (3) no two queens can be on the same diagonal.

## Approach
The solution uses recursion and backtracking to place queens on the board one row at a time, ensuring that each placement is safe from attack by previously placed queens. The algorithm checks for safety by verifying that the new queen does not share a column or diagonal with any existing queen.

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
        vector<int> board(n, -1); // Initialize board with -1
        solveNQueensHelper(result, board, 0);
        return result;
    }
    
    void solveNQueensHelper(vector<vector<string>>& result, vector<int>& board, int row) {
        if (row == board.size()) {
            // If all queens are placed, add the configuration to the result
            vector<string> config;
            for (int i = 0; i < board.size(); i++) {
                string s(board.size(), '.');
                s[board[i]] = 'Q';
                config.push_back(s);
            }
            result.push_back(config);
            return;
        }
        
        for (int col = 0; col < board.size(); col++) {
            if (isValid(board, row, col)) {
                board[row] = col; // Place queen at (row, col)
                solveNQueensHelper(result, board, row + 1); // Recur for the next row
                board[row] = -1; // Backtrack and remove the queen
            }
        }
    }
    
    bool isValid(vector<int>& board, int row, int col) {
        for (int i = 0; i < row; i++) {
            if (board[i] == col || 
                board[i] - i == col - row || 
                board[i] + i == col + row) {
                return false;
            }
        }
        return true;
    }
};

```

## Test Cases
```
Input: n = 4
Output: [
  [".Q..", "...Q", "Q...", "..Q."],
  ["..Q.", "Q...", "...Q", ".Q.."]
]
```

## Key Takeaways
- The N-Queens problem can be solved using recursion and backtracking by placing queens one row at a time and checking for safety.
- The time complexity is O(N!) due to the recursive nature of the solution, where N is the number of queens.
- The space complexity is O(N) for storing the board configuration.