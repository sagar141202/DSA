# Sudoku Solver

## Problem Statement
The Sudoku Solver problem is a classic problem in the field of computer science and puzzle solving. Given a 9x9 Sudoku grid, some of the numbers are already filled in, while others are blank. The goal is to fill in all the blank cells with numbers from 1 to 9 such that each row, column, and 3x3 sub-grid contains each number exactly once. The input grid is represented as a 2D array, where 0 represents a blank cell. The output should be the solved Sudoku grid, if a solution exists.

## Approach
The approach to solve this problem is to use a recursive backtracking algorithm, which tries to fill in each blank cell with a number from 1 to 9 and checks if the current state of the grid is valid. If the current state is valid, it recursively tries to fill in the next blank cell. If the current state is not valid, it backtracks and tries a different number.

## Complexity
- Time: O(9^(n*n)) where n is the size of the grid, in this case, n = 3 for a 9x9 grid.
- Space: O(n*n) for the recursive call stack.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isValid(vector<vector<int>>& board, int row, int col, int num) {
    // check the row
    for (int i = 0; i < 9; i++) {
        if (board[row][i] == num) {
            return false;
        }
    }

    // check the column
    for (int i = 0; i < 9; i++) {
        if (board[i][col] == num) {
            return false;
        }
    }

    // check the 3x3 sub-grid
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

void printBoard(vector<vector<int>>& board) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << board[i][j] << " ";
            if ((j + 1) % 3 == 0 && j < 8) {
                cout << "| ";
            }
        }
        cout << endl;
        if ((i + 1) % 3 == 0 && i < 8) {
            cout << "---------------------" << endl;
        }
    }
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
        printBoard(board);
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
---------------------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
---------------------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9

Output: 
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
---------------------
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
---------------------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
```

## Key Takeaways
- Recursion and backtracking are essential techniques for solving Sudoku-like problems.
- The `isValid` function is crucial in ensuring that the current state of the grid is valid before making a recursive call.
- The `solveSudoku` function uses a recursive approach to fill in the blank cells, and it backtracks when it encounters an invalid state.