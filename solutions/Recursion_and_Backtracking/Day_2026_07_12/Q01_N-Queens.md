# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in computer science where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board that satisfy this condition. For example, for a 4x4 board, there are two possible configurations.

## Approach
The approach to solve this problem involves using recursion and backtracking to try all possible placements of queens on the board. The algorithm starts by placing a queen in the first column and then recursively tries to place queens in the remaining columns, ensuring that each placement is safe from attack by previously placed queens.

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
- The N-Queens problem can be solved using recursion and backtracking.
- The time complexity of the solution is O(N!) due to the recursive nature of the algorithm.
- The space complexity is O(N) for storing the current configuration of the board.