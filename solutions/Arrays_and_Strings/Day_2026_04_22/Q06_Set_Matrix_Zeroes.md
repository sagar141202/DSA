# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you cannot use any extra space that scales with the input size, other than a constant amount. The matrix is modified in-place, and you do not need to return anything.

## Approach
We will use the first row and first column to track which rows and columns need to be zeroed. This approach allows us to avoid using any extra space that scales with the input size. We iterate over the matrix to mark the rows and columns that need to be zeroed, and then we iterate over the matrix again to set the marked rows and columns to zero.

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
    
    bool firstRowZero = false;
    bool firstColZero = false;
    
    // mark rows and cols that need to be zeroed
    for (int i = 0; i < m; i++) {
        if (matrix[i][0] == 0) {
            firstColZero = true;
        }
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                if (i == 0) {
                    firstRowZero = true;
                }
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }
    
    // zero out marked rows and cols
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }
    
    // zero out first row and col if needed
    if (firstRowZero) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }
    if (firstColZero) {
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
- Use the first row and column to track which rows and columns need to be zeroed to avoid using extra space.
- Iterate over the matrix twice: once to mark the rows and columns that need to be zeroed, and once to zero out the marked rows and columns.
- Handle the first row and column as special cases to avoid using extra space.