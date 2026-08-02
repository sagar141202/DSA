# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you are not allowed to use any extra space that scales with the input size. The input matrix is represented as a 2D vector of integers, where each integer represents an element in the matrix. For example, given the following matrix:
```
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
```
The output should be:
```
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```
The constraints are 1 <= m <= 200, 1 <= n <= 200, and the matrix only contains integers 0 and 1.

## Approach
We will use the first row and first column to track the rows and columns that need to be set to zero. We start by checking the first row and column for zeros, then we iterate over the rest of the matrix, marking the corresponding row and column in the first row and column if we encounter a zero. Finally, we set the marked rows and columns to zero.

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

    // Iterate over each row
    for (int i = 0; i < m; i++) {
        // Check if the first column needs to be set to zero
        if (matrix[i][0] == 0) {
            isCol = true;
        }

        // Iterate over each column (excluding the first column)
        for (int j = 1; j < n; j++) {
            // If the current element is zero, mark the row and column
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // Set the marked rows and columns to zero (excluding the first row and column)
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Set the first row to zero if it was marked
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Set the first column to zero if it was marked
    if (isCol) {
        for (int i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
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
- We can use the first row and column to track the rows and columns that need to be set to zero, reducing the space complexity to O(1).
- We need to handle the first row and column separately to avoid overwriting the tracking information.
- The time complexity is O(m*n) because we are iterating over the entire matrix twice.