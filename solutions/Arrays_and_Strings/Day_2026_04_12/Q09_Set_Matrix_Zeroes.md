# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The matrix is modified in-place, and no extra space can be used other than a constant amount of space for variables. For example, given the following matrix: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
the output should be:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
The constraints are 1 <= m <= 200, 1 <= n <= 200.

## Approach
The algorithm uses two variables to track if the first row and column contain zeros. It then iterates over the matrix, marking rows and columns that contain zeros. Finally, it updates the matrix based on the marked rows and columns.

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
    
    // mark rows and cols that need to be zeroed out
    for (int i = 0; i < m; i++) {
        if (matrix[i][0] == 0) isCol = true;
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }
    
    // update matrix based on marked rows and cols
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }
    
    // update first row if needed
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }
    
    // update first col if needed
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
- Use the first row and column to mark which rows and columns need to be zeroed out.
- Update the matrix in two passes to avoid overwriting information.
- Handle the first row and column separately to avoid using extra space.