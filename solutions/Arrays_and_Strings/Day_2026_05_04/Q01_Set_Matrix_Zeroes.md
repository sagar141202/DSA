# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you should not use any extra space that scales with the input size. The matrix is represented as a 2D vector of integers. For example, given the following matrix:
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
We will use two extra arrays to track the rows and columns that need to be zeroed out. We will iterate over the matrix to find the zero elements and mark the corresponding rows and columns in the arrays. Then we will iterate over the matrix again to set the marked rows and columns to zero.

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

    // Find the zero elements and mark the corresponding rows and columns
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i] = true;
                cols[j] = true;
            }
        }
    }

    // Set the marked rows and columns to zero
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
- We can use extra space to track the rows and columns that need to be zeroed out.
- We need to iterate over the matrix twice to find the zero elements and set the marked rows and columns to zero.
- The time complexity is O(m*n) and the space complexity is O(m + n), where m is the number of rows and n is the number of columns.