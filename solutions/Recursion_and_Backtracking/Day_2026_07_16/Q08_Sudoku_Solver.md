# Sudoku Solver

## Problem Statement
The Sudoku Solver problem is a classic backtracking problem where we are given a 9x9 grid, divided into nine 3x3 sub-grids or "regions." Some numbers are already filled in, while others are blank. The goal is to fill in all the blank cells with numbers from 1 to 9 such that each row, column, and region contains each number exactly once. The input is a 2D vector of integers, where 0 represents a blank cell. The output is a boolean indicating whether a solution exists, and if so, the modified input grid contains the solution.

## Approach
The approach is to use a recursive backtracking algorithm to try all possible numbers for each blank cell, checking if the current number is valid in the current position. If it is, we recursively call the function for the next blank cell. If not, we backtrack and try the next number.

## Complexity
- Time: O(9^(n*n)) in the worst case, where n is the size of the grid (9 for a standard Sudoku)
- Space: O(n*n) for the recursive call stack

## C++ Solution
```cpp
#include <vector>
using namespace std;

bool isValid(vector<vector<int>>& board, int row, int col, int num) {
    // Check the row
    for (int x = 0; x < 9; x++) {
        if (board[row][x] == num) {
            return false;
        }
    }

    // Check the column
    for (int x = 0; x < 9; x++) {
        if (board[x][col] == num) {
            return false;
        }
    }

    // Check the box
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i + startRow][j + startCol] == num) {
                return false;
            }
        }
    }
    return true;
}

bool solveSudoku(vector<vector<int>>& board) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == 0) {
                for (int num = 1; num <= 9; num++) {
                    if (isValid(board, i, j, num)) {
                        board[i][j] = num;
                        if (solveSudoku(board)) {
                            return true;
                        }
                        board[i][j] = 0;
                    }
                }
                return false;
            }
        }
    }
    return true;
}

int main() {
    vector<vector<int>> board = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };

    if (solveSudoku(board)) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "No solution exists" << endl;
    }

    return 0;
}
```

## Test Cases
```
Input: 
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

Output: 
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

## Key Takeaways
- The Sudoku Solver problem is a classic example of a backtracking problem, where we try all possible solutions and backtrack when we reach a dead end.
- The `isValid` function is used to check if a number is valid in a given position, by checking the row, column, and box.
- The `solveSudoku` function uses recursion to try all possible numbers for each blank cell, and backtracks when a solution is not found.