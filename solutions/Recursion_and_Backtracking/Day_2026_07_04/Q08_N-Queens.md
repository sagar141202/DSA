# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem requires finding all possible configurations of the board where N queens can be placed safely. The input is an integer N, representing the size of the chessboard, and the output is a list of all possible configurations.

## Approach
The approach to solve this problem is to use backtracking and recursion. We start by placing the first queen in the first row, then recursively try to place the remaining queens in the subsequent rows, ensuring that no two queens attack each other. If a safe position is found, we move on to the next row; otherwise, we backtrack and try a different position.

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
        vector<int> queens(n, -1);
        solve(n, 0, queens, result);
        return result;
    }

    void solve(int n, int row, vector<int>& queens, vector<vector<string>>& result) {
        if (row == n) {
            vector<string> board(n, string(n, '.'));
            for (int i = 0; i < n; i++) {
                board[i][queens[i]] = 'Q';
            }
            result.push_back(board);
            return;
        }
        for (int col = 0; col < n; col++) {
            if (isValid(n, row, col, queens)) {
                queens[row] = col;
                solve(n, row + 1, queens, result);
            }
        }
    }

    bool isValid(int n, int row, int col, vector<int>& queens) {
        for (int i = 0; i < row; i++) {
            if (queens[i] == col || 
                queens[i] - i == col - row || 
                queens[i] + i == col + row) {
                return false;
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
- The N-Queens problem is a classic example of a backtracking problem, where we need to try all possible configurations and backtrack when a dead end is reached.
- The time complexity of the solution is O(N!), which is the number of possible configurations of the board.
- The space complexity is O(N), which is the maximum depth of the recursion call stack.