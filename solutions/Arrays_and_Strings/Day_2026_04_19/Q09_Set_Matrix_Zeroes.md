# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you should not use any extra space that scales with the input size. The input matrix will have at most 100 rows and at most 100 columns. For example, given the following matrix: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
After calling the function, the matrix should be:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

## Approach
The algorithm uses the first row and first column to track which rows and columns should be zeroed. It iterates over the matrix to mark the rows and columns, then it iterates again to set the marked rows and columns to zero. This approach allows for in-place modification without using extra space that scales with the input size.

## Complexity
- Time: O(m*n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

void setZeroes(std::vector<std::vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    bool isCol = false;

    for (int i = 0; i < m; i++) {
        // Check if the first column needs to be zeroed
        if (matrix[i][0] == 0) isCol = true;
        
        // Iterate over the rest of the row
        for (int j = 1; j < n; j++) {
            // If the current element is zero, mark the row and column
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0; // Mark the column
                matrix[i][0] = 0; // Mark the row
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

    // Zero out the first row if needed
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Zero out the first column if needed
    if (isCol) {
        for (int i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
}

int main() {
    std::vector<std::vector<int>> matrix = {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1}
    };

    setZeroes(matrix);

    // Print the modified matrix
    for (const auto& row : matrix) {
        for (int val : row) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }

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
- Use the first row and first column to track which rows and columns should be zeroed.
- Iterate over the matrix twice: once to mark the rows and columns, and again to set the marked rows and columns to zero.
- Handle the first row and first column as special cases to ensure they are properly zeroed if needed.