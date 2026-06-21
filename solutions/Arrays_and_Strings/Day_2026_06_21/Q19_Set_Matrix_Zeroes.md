# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The input matrix is modified in-place, and no extra space can be used other than a constant amount. For example, given the following matrix: 
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
The constraints are 1 <= m <= 200, 1 <= n <= 200, and the matrix is modified in-place.

## Approach
The approach is to use the first row and first column to track which rows and columns need to be set to zero. We iterate over the matrix, and if we find a zero, we mark the corresponding row and column in the first row and column.

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

    // handle first row and col
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
- Use the first row and column to track which rows and columns need to be set to zero.
- Handle the first row and column separately to avoid overwriting important information.
- The solution has a time complexity of O(m * n) and a space complexity of O(1), making it efficient for large matrices.