# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The input matrix is modified in-place, and no extra space can be used other than constant space. For example, given the following matrix:
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
The constraints are: 1. m == matrix.length, 2. n == matrix[0].length, 3. 1 <= m, n <= 200, 4. -2^31 <= matrix[i][j] <= 2^31 - 1.

## Approach
We use the first row and first column as flags to track which rows and columns need to be zeroed out. We iterate through the matrix and mark the corresponding row and column flags if we encounter a zero. Then we iterate through the matrix again and set the rows and columns to zero based on the flags.

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
        // Check if the first column needs to be zeroed out
        if (matrix[i][0] == 0) {
            isCol = true;
        }
        for (int j = 1; j < n; j++) {
            // If the current element is zero, set the first element of the row and column to zero
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // Zero out the rows and columns based on the flags
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero out the first row if it was marked
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Zero out the first column if it was marked
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
- We use the input matrix itself as extra space to track which rows and columns need to be zeroed out.
- The time complexity is O(m * n) because we make two passes through the matrix.
- The space complexity is O(1) because we only use a constant amount of space to store the flags.