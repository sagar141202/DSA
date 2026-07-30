# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The input matrix is modified in-place to produce the output. For example, given the following matrix:
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
The constraints are 1 <= m <= 200, 1 <= n <= 200, and the matrix only contains integers 0 and 1.

## Approach
The approach is to use two vectors to keep track of rows and columns that need to be set to zero. We then iterate through the matrix to find the zeros and mark the corresponding rows and columns. Finally, we set the marked rows and columns to zero.

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

    // mark rows and cols that need to be zeroed
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i] = true;
                cols[j] = true;
            }
        }
    }

    // zero out the marked rows and cols
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
- We can solve this problem in O(m * n) time complexity where m is the number of rows and n is the number of columns.
- We need O(m + n) extra space to store the rows and columns that need to be zeroed.
- The key idea is to mark the rows and columns that need to be zeroed in the first pass, and then zero them out in the second pass.