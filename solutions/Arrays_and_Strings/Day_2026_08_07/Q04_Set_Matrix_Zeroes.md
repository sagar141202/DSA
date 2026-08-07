# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you should not use any extra space that scales with the input size, other than a constant amount of space for variables. The matrix is modified in-place.

## Approach
We iterate over the matrix to find the rows and columns that contain zeros, then we set those rows and columns to zero. We use two arrays to keep track of the rows and columns to be zeroed. 

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

    // Find the rows and columns that need to be zeroed
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i] = true;
                cols[j] = true;
            }
        }
    }

    // Zero out the rows and columns
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
- Use extra space to store the rows and columns to be zeroed if in-place is not strictly required.
- The solution can be optimized to use the first row and column of the matrix as the arrays to keep track of the rows and columns to be zeroed, thus reducing the space complexity to O(1) if the input matrix can be modified.