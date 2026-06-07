# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, fill it with numbers from 1 to m*n in a spiral order, starting from the top left and moving clockwise. The matrix is filled row by row from left to right and top to bottom. For example, given a 3x3 matrix, the spiral order would be: 
[
  [1, 2, 3],
  [8, 9, 4],
  [7, 6, 5]
]
The input will be the number of rows (m) and columns (n) in the matrix.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to keep track of the current boundaries of the matrix. It fills the matrix in a spiral order by iterating over the elements in a clockwise direction. The pointers are updated after each iteration to move towards the center of the matrix.

## Complexity
- Time: O(m*n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

vector<vector<int>> generateMatrix(int m, int n) {
    vector<vector<int>> matrix(m, vector<int>(n, 0));
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    int num = 1;
    while (top <= bottom && left <= right) {
        // fill the top row from left to right
        for (int i = left; i <= right; i++) {
            matrix[top][i] = num++;
        }
        top++;
        
        // fill the right column from top to bottom
        for (int i = top; i <= bottom; i++) {
            matrix[i][right] = num++;
        }
        right--;
        
        // fill the bottom row from right to left
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                matrix[bottom][i] = num++;
            }
            bottom--;
        }
        
        // fill the left column from bottom to top
        if (left <= right) {
            for (int i = bottom; i >= top; i--) {
                matrix[i][left] = num++;
            }
            left++;
        }
    }
    return matrix;
}
```

## Test Cases
```
Input: m = 3, n = 3
Output: [
  [1, 2, 3],
  [8, 9, 4],
  [7, 6, 5]
]
```

## Key Takeaways
- Use four pointers to keep track of the current boundaries of the matrix.
- Fill the matrix in a spiral order by iterating over the elements in a clockwise direction.
- Update the pointers after each iteration to move towards the center of the matrix.