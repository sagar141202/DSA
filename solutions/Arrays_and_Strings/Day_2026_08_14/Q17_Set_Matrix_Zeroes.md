# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you cannot use any extra space that scales with the input size, other than a constant amount of space to store variables. The matrix is modified in-place, and you do not need to return anything. The input matrix will have dimensions m x n, where 1 <= m, n <= 200. The values in the matrix will be in the range [0, 2^31 - 1].

## Approach
The approach to solve this problem is to use the first row and first column of the matrix as extra space to track which rows and columns need to be zeroed. We iterate through the matrix to find the zeros and mark the corresponding rows and columns in the first row and column. Then, we iterate through the matrix again to set the marked rows and columns to zero.

## Complexity
- Time: O(m * n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

void setZeroes(std::vector<std::vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    bool isCol = false;

    for (int i = 0; i < m; i++) {
        // Check if the first column has a zero
        if (matrix[i][0] == 0) {
            isCol = true;
        }

        // Check the rest of the columns
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                // Mark the row and column to be zeroed
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // Zero out the marked rows and columns
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero out the first row if it was marked
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Zero out the first column if it was marked
    if (isCol) {
        for (int i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
}

int main() {
    std::vector<std::vector<int>> matrix = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
    setZeroes(matrix);
    return 0;
}
```

## Test Cases
```
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

## Key Takeaways
- We can use the first row and first column of the matrix as extra space to track which rows and columns need to be zeroed.
- We need to handle the first row and column separately to avoid overwriting the tracking information.
- The time complexity is O(m * n) because we are iterating through the matrix twice, and the space complexity is O(1) because we are using a constant amount of space to store variables.