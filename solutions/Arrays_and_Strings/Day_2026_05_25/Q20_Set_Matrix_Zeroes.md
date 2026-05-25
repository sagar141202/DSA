# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The matrix is modified in-place, and no extra space can be used other than a constant amount. For example, given the following matrix: 
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
The constraints are 1 <= m <= 200, 1 <= n <= 200, and -2^31 <= matrix[i][j] <= 2^31 - 1.

## Approach
The algorithm uses the first row and first column to track which rows and columns should be zeroed. It iterates over the matrix to identify the rows and columns that need to be zeroed and marks them in the first row and column. Then it iterates over the matrix again to set the marked rows and columns to zero.

## Complexity
- Time: O(m * n)
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
        // Mark columns that need to be zeroed in the first row
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // Zero out marked rows and columns
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero out the first row if necessary
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Zero out the first column if necessary
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
- We use the first row and column to track which rows and columns need to be zeroed.
- We iterate over the matrix twice: once to mark the rows and columns that need to be zeroed, and once to zero them out.
- We handle the first row and column separately to avoid overwriting the tracking information.