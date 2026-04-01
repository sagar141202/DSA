# Sudoku Solver

## Problem Statement
The Sudoku Solver problem is a classic backtracking problem where we are given a 9x9 grid, with some numbers already filled in. The goal is to fill in the remaining empty cells with numbers from 1 to 9, such that each row, column, and 3x3 sub-grid contains each number exactly once. The input grid is represented as a 2D array, where empty cells are denoted by 0. The output should be the solved grid, or a message indicating that no solution exists. For example, given the following grid:
```
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
-------------------------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
-------------------------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9
```
We need to fill in the empty cells to get a valid Sudoku solution.

## Approach
The approach to solve this problem is to use recursion and backtracking. We start by filling in the first empty cell with a number from 1 to 9, and then recursively try to fill in the rest of the grid. If we reach a point where we cannot fill in a cell, we backtrack and try a different number.

## Complexity
- Time: O(9^(n*n)) where n is the size of the grid, as in the worst case, we have to try all possible numbers for each cell.
- Space: O(n*n) for the recursive call stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isValid(int board[9][9], int row, int col, int num) {
    // Check the row
    for (int i = 0; i < 9; i++) {
        if (board[row][i] == num) {
            return false;
        }
    }

    // Check the column
    for (int i = 0; i < 9; i++) {
        if (board[i][col] == num) {
            return false;
        }
    }

    // Check the box
    int boxRow = row - row % 3;
    int boxCol = col - col % 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[boxRow + i][boxCol + j] == num) {
                return false;
            }
        }
    }

    return true;
}

bool solveSudoku(int board[9][9]) {
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
    int board[9][9] = {
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
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
-------------------------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
-------------------------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9

Output:
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
-------------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
-------------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

## Key Takeaways
- Use recursion and backtracking to solve the Sudoku puzzle.
- The `isValid` function checks if it's possible to place a number in a given cell.
- The `solveSudoku` function tries to fill in the Sudoku grid by recursively trying different numbers for each empty cell.