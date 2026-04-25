# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the field of computer science, where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board where the queens are placed safely. For example, for a 4x4 board, there are two possible configurations.

## Approach
The approach to solve this problem is to use backtracking, where we try to place a queen in each column of the board, one by one. We use a recursive function to place the queens, and we check for each placement if it is safe or not. If it is safe, we move on to the next column, otherwise, we backtrack and try a different placement.

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
        vector<int> board(n, -1);
        solveNQueensHelper(n, 0, board, result);
        return result;
    }

    void solveNQueensHelper(int n, int row, vector<int>& board, vector<vector<string>>& result) {
        if (row == n) {
            vector<string> solution;
            for (int i = 0; i < n; i++) {
                string s(n, '.');
                s[board[i]] = 'Q';
                solution.push_back(s);
            }
            result.push_back(solution);
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isSafe(n, row, col, board)) {
                board[row] = col;
                solveNQueensHelper(n, row + 1, board, result);
            }
        }
    }

    bool isSafe(int n, int row, int col, vector<int>& board) {
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

int main() {
    Solution solution;
    int n = 4;
    vector<vector<string>> result = solution.solveNQueens(n);
    for (auto& solution : result) {
        for (auto& row : solution) {
            cout << row << endl;
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
- The N-Queens problem is a classic example of a backtracking problem, where we try to place queens on a board and backtrack when a placement is not safe.
- The time complexity of the solution is O(N!), where N is the number of queens, because we try all possible placements of the queens.
- The space complexity of the solution is O(N), where N is the number of queens, because we need to store the current state of the board.