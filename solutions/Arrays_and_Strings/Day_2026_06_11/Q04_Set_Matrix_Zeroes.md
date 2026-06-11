# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do not return anything, but modify the matrix in-place. The matrix is represented by a 2D vector of integers. For example, given the following matrix:
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
The constraints are: m == matrix.length, n == matrix[0].length, 1 <= m, n <= 200, -2^31 <= matrix[i][j] <= 2^31 - 1.

## Approach
We will use a two-pass approach to solve this problem. First, we mark the rows and columns that need to be zeroed. Then, we iterate through the matrix again to set the marked rows and columns to zero.

## Complexity
- Time: O(m*n)
- Space: O(m + n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

void setZeroes(vector<vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    vector<bool> rows(m, false);
    vector<bool> cols(n, false);
    
    // Mark rows and cols that need to be zeroed
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i] = true;
                cols[j] = true;
            }
        }
    }
    
    // Set marked rows and cols to zero
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (rows[i] || cols[j]) {
                matrix[i][j] = 0;
            }
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
- We use two additional vectors to keep track of rows and columns that need to be zeroed.
- We make two passes through the matrix: one to mark the rows and columns, and another to set them to zero.
- The space complexity can be optimized to O(1) by using the first row and column of the matrix to mark the rows and columns, but this would make the code more complex.