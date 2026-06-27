# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you cannot use any additional space that scales with the input size, except for a constant amount of extra memory. The input matrix will be modified in-place to be the resulting matrix. For example, given the following matrix: 
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
The constraints are 1 <= m <= 200, 1 <= n <= 200, and the values in the matrix will be either 0 or 1.

## Approach
The algorithm involves first identifying the rows and columns that need to be zeroed out by checking for 0s in the matrix. We use the first row and column to keep track of the rows and columns to be zeroed. Then we make a second pass over the matrix to zero out the marked rows and columns.

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

    // Mark rows and cols to be zeroed
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

    // Zero out first row and col if needed
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }
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
- The solution uses the first row and column as extra space to track which rows and columns to zero out.
- A second pass is made over the matrix to zero out the marked rows and columns.
- Special care is taken to handle the first row and column separately to avoid using extra space.