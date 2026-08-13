# Sudoku Solver

## Problem Statement
Given a partially filled Sudoku grid, the task is to fill in the missing numbers so that each row, column, and 3x3 sub-grid contains the numbers 1-9 without repeating any number. The input grid is a 9x9 2D array, where 0 represents an empty cell. The goal is to find a solution that satisfies the standard Sudoku rules.

## Approach
The algorithm uses recursion and backtracking to try different numbers in each empty cell. It checks for validity at each step, ensuring that the current number does not already exist in the same row, column, or 3x3 sub-grid. If a valid solution is found, the function returns true; otherwise, it backtracks and tries alternative numbers.

## Complexity
- Time: O(9^(n*n)) where n is the size of the grid (9x9 in this case), due to the recursive nature of the algorithm and the possibility of trying all numbers in each cell.
- Space: O(n*n) for the recursive call stack in the worst case.

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isValid(int board[9][9], int row, int col, int num) {
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
- Recursion and backtracking are powerful tools for solving puzzles like Sudoku, where trying all possible combinations is necessary.
- The isValid function is crucial for ensuring that each number placement adheres to Sudoku rules, preventing incorrect solutions.
- This solution modifies the input grid in-place to fill in the missing numbers, providing a clear and concise way to visualize the solved puzzle.