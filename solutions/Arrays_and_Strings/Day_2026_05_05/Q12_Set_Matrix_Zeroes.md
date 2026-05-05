# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you should not use any extra space that scales with the input size. The input matrix is represented as a 2D vector of integers. For example, given the following matrix:
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
The constraints are 1 <= m <= 200, 1 <= n <= 200, and the matrix only contains integers 0 or 1.

## Approach
The approach to solve this problem is to use the first row and first column as extra space to track which rows and columns need to be set to zero. We iterate through the matrix to mark the rows and columns that need to be zeroed. Then we iterate through the matrix again to set the marked rows and columns to zero.

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

    // mark rows and cols that need to be zeroed
    for (int i = 0; i < m; i++) {
        if (matrix[i][0] == 0) isCol = true;
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // set marked rows and cols to zero
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // set first row to zero if needed
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // set first col to zero if needed
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
- We use the first row and first column to track which rows and columns need to be set to zero, thus avoiding the need for extra space.
- We iterate through the matrix twice: once to mark the rows and columns that need to be zeroed, and once to set the marked rows and columns to zero.
- The time complexity is O(m*n) because we iterate through the matrix twice, and the space complexity is O(1) because we only use a constant amount of extra space.