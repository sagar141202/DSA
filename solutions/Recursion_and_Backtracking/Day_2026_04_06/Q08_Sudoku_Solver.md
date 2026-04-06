# Sudoku Solver

## Problem Statement
The Sudoku Solver problem is a classic problem in the realm of recursion and backtracking. We are given a 9x9 grid, with some numbers already filled in and some blank cells. The goal is to fill in all the blank cells with numbers from 1 to 9, such that each row, column, and 3x3 sub-grid contains each number exactly once. The input will be a 2D vector of integers, where 0 represents a blank cell. The output will be a boolean indicating whether a solution exists, and if so, the modified input grid will contain the solution.

## Approach
The approach to solve this problem is to use recursion and backtracking. We will start by filling in the first blank cell with a number from 1 to 9, and then recursively try to fill in the rest of the grid. If we find a number that works, we move on to the next blank cell. If we can't find a number that works, we backtrack and try a different number for the previous cell.

## Complexity
- Time: O(9^(n*n)) where n is the size of the grid (9 in this case), because in the worst case, we have to try all possible numbers for each cell.
- Space: O(n*n) for the recursive call stack, where n is the size of the grid.

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
- Recursion and backtracking can be used to solve complex problems by breaking them down into smaller sub-problems.
- The key to solving Sudoku is to use a recursive approach to try all possible numbers for each blank cell, and to use backtracking to undo the changes when a dead end is reached.
- The `isValid` function is used to check if a number can be placed in a given cell, by checking the row, column, and 3x3 sub-grid.