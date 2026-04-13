# Sudoku Solver

## Problem Statement
Given a 9x9 Sudoku grid, some of the numbers are already filled in, while others are blank. The task is to fill in all the blank cells with numbers from 1 to 9 such that each row, column, and 3x3 sub-grid contains each number exactly once. The input grid is represented as a 2D vector of characters, where '.' represents a blank cell. The output should be the solved grid, if a solution exists.

## Approach
The approach is to use recursion and backtracking to try all possible numbers for each blank cell. The algorithm checks if the current number is valid in the current cell, and if so, recursively tries to fill in the rest of the grid. If it cannot find a valid number for a cell, it backtracks and tries a different number.

## Complexity
- Time: O(9^(n*n)) where n is the size of the grid (in this case, n=3 for a 9x9 grid)
- Space: O(n*n) for the recursive call stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isValid(vector<vector<char>>& board, int row, int col, char num) {
    // check the row
    for (int i = 0; i < 9; i++) {
        if (board[row][i] == num) return false;
    }
    // check the column
    for (int i = 0; i < 9; i++) {
        if (board[i][col] == num) return false;
    }
    // check the 3x3 sub-grid
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i + startRow][j + startCol] == num) return false;
        }
    }
    return true;
}

bool solveSudoku(vector<vector<char>>& board) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (board[i][j] == '.') {
                for (char num = '1'; num <= '9'; num++) {
                    if (isValid(board, i, j, num)) {
                        board[i][j] = num;
                        if (solveSudoku(board)) return true;
                        board[i][j] = '.';
                    }
                }
                return false;
            }
        }
    }
    return true;
}

void printBoard(vector<vector<char>>& board) {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << board[i][j] << " ";
            if ((j + 1) % 3 == 0 && j < 8) cout << "| ";
        }
        cout << endl;
        if ((i + 1) % 3 == 0 && i < 8) cout << "- - - - - - - - - - - -" << endl;
    }
}

int main() {
    vector<vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
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
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

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
- The Sudoku Solver problem is a classic example of a problem that can be solved using recursion and backtracking.
- The key to solving this problem is to use a helper function to check if a given number is valid in a given cell.
- The algorithm tries all possible numbers for each blank cell, and if it cannot find a valid number, it backtracks and tries a different number.