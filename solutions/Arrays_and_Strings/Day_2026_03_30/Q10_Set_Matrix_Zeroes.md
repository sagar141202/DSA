# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do not return anything, modify the matrix in-place. The matrix is modified in-place, meaning that the changes are made directly to the input matrix without creating a new one. For example, given the following matrix:
```
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
```
After calling the function, the matrix should be:
```
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
```
Constraints: m == matrix.length, n == matrix[0].length, 1 <= m, n <= 200, -2^31 <= matrix[i][j] <= 2^31 - 1.

## Approach
The algorithm uses two sets to keep track of the rows and columns that need to be zeroed out. It iterates over the matrix to find the zeros, then iterates again to set the corresponding rows and columns to zero.

## Complexity
- Time: O(m * n)
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

    // first pass: find the rows and cols that need to be zeroed out
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i] = true;
                cols[j] = true;
            }
        }
    }

    // second pass: set the corresponding rows and cols to zero
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
- Use two separate data structures (in this case, vectors of booleans) to keep track of the rows and columns that need to be zeroed out.
- Make two passes over the matrix: one to find the zeros, and another to set the corresponding rows and columns to zero.
- This solution has a time complexity of O(m * n) and a space complexity of O(m + n), where m is the number of rows and n is the number of columns in the matrix.