# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The input matrix is modified in-place, and no extra space can be used other than a constant amount of space for variables. The matrix consists of integers, and the size of the matrix is known. For example, given the following matrix: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
After calling the function, the matrix should be:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

## Approach
We will use two flags to track whether the first row and column contain zeros. Then we will use the first row and column to mark other rows and columns that need to be zeroed. Finally, we will zero out the marked rows and columns.

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
    bool firstRowZero = false;
    bool firstColZero = false;

    // Check if the first row contains a zero
    for (int i = 0; i < n; i++) {
        if (matrix[0][i] == 0) {
            firstRowZero = true;
            break;
        }
    }

    // Check if the first column contains a zero
    for (int i = 0; i < m; i++) {
        if (matrix[i][0] == 0) {
            firstColZero = true;
            break;
        }
    }

    // Use the first row and column to mark other rows and columns that need to be zeroed
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // Zero out the marked rows and columns
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Zero out the first row and column if necessary
    if (firstRowZero) {
        for (int i = 0; i < n; i++) {
            matrix[0][i] = 0;
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
- Use extra space efficiently to store flags for rows and columns.
- Modify the input matrix in-place by using the first row and column to mark other rows and columns that need to be zeroed.
- Handle edge cases such as when the input matrix is empty or contains only one row or column.