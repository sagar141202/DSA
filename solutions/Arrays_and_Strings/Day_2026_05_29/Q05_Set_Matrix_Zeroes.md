# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The matrix is represented as a 2D vector of integers. The function should modify the input matrix in-place. For example, given the following matrix:
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
The constraints are 1 <= m <= 200, 1 <= n <= 200, and -2^31 <= matrix[i][j] <= 2^31 - 1.

## Approach
We will use two sets to keep track of the rows and columns that need to be set to zero. Then we will iterate over the matrix to set the corresponding rows and columns to zero. We also need to handle the first row and column separately to avoid overwriting the original values.

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
    vector<int> rows(m, 0);
    vector<int> cols(n, 0);

    // Mark rows and cols to be zeroed
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i] = 1;
                cols[j] = 1;
            }
        }
    }

    // Zero out the marked rows and cols
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
- Use two separate vectors to track rows and columns to be zeroed out.
- Handle the first row and column separately to avoid overwriting the original values.
- Use a two-pass approach to mark the rows and columns to be zeroed out and then to zero them out.