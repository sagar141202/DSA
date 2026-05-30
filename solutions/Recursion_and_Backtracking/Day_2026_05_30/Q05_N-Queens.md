# N-Queens

## Problem Statement
The N-Queens problem is a classic problem of placing N queens on an NxN chessboard such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally. The problem statement requires finding all possible configurations of placing N queens on the board. The constraints are 1 ≤ N ≤ 9, and the input is an integer N. For example, for N = 4, the output should be all possible configurations where 4 queens are placed on a 4x4 chessboard without any queen attacking another.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start by placing a queen in the first column and then recursively try to place queens in the remaining columns. If a queen cannot be placed in any row of the current column without being attacked, we backtrack and try a different row in the previous column.

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
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 'Q') return false;
            if (col - (row - i) >= 0 && board[i][col - (row - i)] == 'Q') return false;
            if (col + (row - i) < board.size() && board[i][col + (row - i)] == 'Q') return false;
        }
        return true;
    }
};

int main() {
    Solution solution;
    vector<vector<string>> result = solution.solveNQueens(4);
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
- Use recursion and backtracking to solve the N-Queens problem.
- The time complexity is O(N!) due to the recursive nature of the solution.
- The space complexity is O(N) for storing the board configuration.