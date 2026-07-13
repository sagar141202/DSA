# Spiral Matrix

## Problem Statement
Given a matrix of size m x n, fill it with numbers from 1 to m*n in a spiral order, starting from the top left and moving clockwise. The matrix is filled row by row from left to right and top to bottom. For example, given a 3x3 matrix, the spiral order is: [ [1, 2, 3], [8, 9, 4], [7, 6, 5] ]. The input will be the number of rows (m) and columns (n) in the matrix.

## Approach
The algorithm uses four pointers (top, bottom, left, right) to traverse the matrix in a spiral order. It starts by filling the top row from left to right, then the right column from top to bottom, then the bottom row from right to left, and finally the left column from bottom to top. This process continues until all elements are filled.

## Complexity
- Time: O(m*n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

std::vector<std::vector<int>> generateMatrix(int m, int n) {
    std::vector<std::vector<int>> matrix(m, std::vector<int>(n, 0));
    int top = 0, bottom = m - 1, left = 0, right = n - 1;
    int num = 1;
    
    while (top <= bottom && left <= right) {
        // Fill top row from left to right
        for (int i = left; i <= right; i++) {
            matrix[top][i] = num++;
        }
        top++;
        
        // Fill right column from top to bottom
        for (int i = top; i <= bottom; i++) {
            matrix[i][right] = num++;
        }
        right--;
        
        // Fill bottom row from right to left
        if (top <= bottom) {
            for (int i = right; i >= left; i--) {
                matrix[bottom][i] = num++;
            }
            bottom--;
        }
        
        // Fill left column from bottom to top
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
Output: [ [1, 2, 3], [8, 9, 4], [7, 6, 5] ]
Input: m = 4, n = 4
Output: [ [1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7] ]
```

## Key Takeaways
- Use four pointers to traverse the matrix in a spiral order.
- Fill the matrix row by row and column by column, changing the direction after each iteration.
- Continue the process until all elements are filled.