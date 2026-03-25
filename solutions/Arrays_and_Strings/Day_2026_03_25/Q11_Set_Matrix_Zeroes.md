# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, i.e., without using any extra space that scales with the input size. The matrix is represented as a 2D vector of integers. For example, given the following matrix:
```
[
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
```
The output should be:
```
[
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
```
The constraints are: m == matrix.length, n == matrix[0].length, 1 <= m, n <= 200, -2^31 <= matrix[i][j] <= 2^31 - 1.

## Approach
The algorithm will iterate over the matrix to find the zeroes, then use the first row and column to track which rows and columns need to be set to zero. It will then set the corresponding rows and columns to zero.

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

    for (int i = 0; i < m; i++) {
        // Check if the first column has a zero
        if (matrix[i][0] == 0) {
            isCol = true;
        }
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                // Use the first row and column to track zeroes
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                // Set the corresponding cell to zero
                matrix[i][j] = 0;
            }
        }
    }

    // Check if the first row needs to be set to zero
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Check if the first column needs to be set to zero
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
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
Output:
[
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
```

## Key Takeaways
- Use the first row and column to track which rows and columns need to be set to zero to avoid using extra space.
- Handle the first row and column separately to avoid overwriting the tracking information.
- Set the corresponding cells to zero based on the tracking information in the first row and column.