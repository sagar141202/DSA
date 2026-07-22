# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The matrix is modified in-place, and no extra space can be used other than a constant amount for variables. The input matrix will have dimensions mxn, where 1 <= m, n <= 200. The elements in the matrix will be integers between 0 and 2^31 - 1.

## Approach
We use the first row and first column as extra space to track which rows and columns need to be set to zero. We then iterate over the matrix, marking the rows and columns that contain zeros. Finally, we set the marked rows and columns to zero.

## Complexity
- Time: O(mn)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    bool isCol = false;

    // Mark rows and cols that need to be zeroed
    for (int i = 0; i < m; i++) {
        if (matrix[i][0] == 0) isCol = true;
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // Zero out marked rows and cols
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Handle first row
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Handle first col
    if (isCol) {
        for (int i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
}

```

## Test Cases
```
Input: [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: [
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```

## Key Takeaways
- We can use the input matrix itself as extra space to track which rows and columns need to be set to zero.
- We handle the first row and column separately because they are used to track which rows and columns need to be zeroed.
- The solution has a time complexity of O(mn) and a space complexity of O(1).