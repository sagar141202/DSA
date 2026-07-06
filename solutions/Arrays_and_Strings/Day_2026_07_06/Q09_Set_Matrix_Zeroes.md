# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning that you should not use any extra space that scales with the input size. The matrix is represented as a 2D array of integers. For example, given the following matrix:
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
The constraints are: m == matrix.length, n == matrix[0].length, 1 <= m, n <= 200, and -2^31 <= matrix[i][j] <= 2^31 - 1.

## Approach
We will use the first row and first column to track the rows and columns that need to be set to 0. We iterate through the matrix to find the zeros and mark the corresponding rows and columns. Then we set the marked rows and columns to 0.

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

    // Iterate through the matrix to find the zeros
    for (int i = 0; i < m; i++) {
        // Check if the first column needs to be set to 0
        if (matrix[i][0] == 0) {
            isCol = true;
        }
        // Mark the rows and columns that need to be set to 0
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // Set the marked rows and columns to 0
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Set the first row to 0 if it was marked
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Set the first column to 0 if it was marked
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
- We use the first row and first column to track the rows and columns that need to be set to 0.
- We iterate through the matrix twice to avoid using extra space.
- We handle the edge cases where the first row or first column needs to be set to 0 separately.