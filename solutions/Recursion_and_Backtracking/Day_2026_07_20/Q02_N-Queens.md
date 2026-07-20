# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the field of computer science, where the goal is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The problem requires finding all possible configurations of the board that satisfy this condition. For example, for a 4x4 board, there are two possible solutions: 
```
. Q . .
. . . Q
Q . . .
. . Q .
```
and
```
. . Q .
Q . . .
. . . Q
. Q . .
```
The input is an integer N, representing the size of the chessboard. The output should be a list of all possible board configurations that satisfy the condition.

## Approach
The solution uses a recursive backtracking approach to try all possible placements of queens on the board. It starts by placing the first queen in the first column, then recursively tries to place the remaining queens in the next columns. If a placement is not valid, it backtracks and tries a different placement.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <vector>
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
            for (int j = 0; j < board.size(); j++) {
                if (board[i][j] == 'Q' && (j == col || abs(i - row) == abs(j - col))) {
                    return false;
                }
            }
        }
        return true;
    }
};
```

## Test Cases
```
Input: 4
Output: [[".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."]]
```

## Key Takeaways
- The N-Queens problem is a classic example of a problem that can be solved using recursive backtracking.
- The key to solving this problem is to ensure that each placement of a queen is valid, meaning it does not attack any previously placed queens.
- The time complexity of the solution is O(N!), where N is the size of the chessboard, because there are N! possible configurations of the board.