# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The matrix is modified in-place, and no extra space can be used other than a constant amount of space for variables. For example, given the following matrix: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
The output should be: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
The constraints are 1 <= m <= 200, 1 <= n <= 200, and the values in the matrix are either 0 or 1.

## Approach
We use the first row and first column to track which rows and columns need to be set to zero. We then iterate over the rest of the matrix, and if we encounter a zero, we mark the corresponding row and column in the first row and column. Finally, we set the marked rows and columns to zero.

## Complexity
- Time: O(m*n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    bool isCol = false;

    // Iterate over the matrix to mark rows and columns that need to be zeroed
    for (int i = 0; i < m; i++) {
        // Check if the first column needs to be zeroed
        if (matrix[i][0] == 0) {
            isCol = true;
        }
        // Mark rows and columns that need to be zeroed
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // Set marked rows and columns to zero
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Set the first row to zero if necessary
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Set the first column to zero if necessary
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
- We can use the first row and first column to track which rows and columns need to be set to zero, reducing the space complexity to O(1).
- The algorithm has a time complexity of O(m*n), where m and n are the dimensions of the matrix.
- The solution modifies the input matrix in-place, without using any extra space other than a constant amount of space for variables.