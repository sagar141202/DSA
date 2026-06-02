# N-Queens

## Problem Statement
The N-Queens problem is a classic problem in the realm of computer science and chess. The problem statement is as follows: Given an NxN chessboard, place N queens on the board such that no two queens attack each other. A queen can attack another queen if they are in the same row, column, or diagonal. The task is to find all possible configurations of the board where N queens can be placed without any of them attacking each other. For example, for a 4x4 chessboard, there are two possible configurations: 
[
    [".Q..", "...Q", "Q...", "..Q."],
    ["..Q.", "Q...", "...Q", ".Q.."]
]
The constraints for this problem are that the input will be a positive integer N, representing the size of the chessboard.

## Approach
The approach to solve this problem involves using recursion and backtracking to try all possible placements of queens on the board. We will use a helper function to check if a queen can be safely placed at a given position on the board. If it can, we will recursively try to place the rest of the queens on the board.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <vector>
#include <string>

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
- The N-Queens problem is a classic example of a problem that can be solved using recursion and backtracking.
- The time complexity of this solution is O(N!) because in the worst case, we have to try all possible permutations of queens on the board.
- The space complexity is O(N) because we need to store the current state of the board, which requires O(N) space.