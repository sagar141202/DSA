# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The input matrix is modified in-place, and no extra space can be used other than a constant amount for variables. For example, given the following matrix: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
The output should be:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
The constraints are 1 <= m <= 200, 1 <= n <= 200, and the matrix only contains integers 0 and 1.

## Approach
We will use the first row and first column to track which rows and columns need to be set to 0. This approach allows us to avoid using extra space that scales with the input size. We will iterate through the matrix, marking the rows and columns that need to be zeroed. Then, we will make a second pass to set the marked rows and columns to 0.

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

    // iterate through the matrix, marking rows and cols that need to be zeroed
    for (int i = 0; i < m; i++) {
        // check if the first column needs to be zeroed
        if (matrix[i][0] == 0) isCol = true;
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                // mark the row and column to be zeroed
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // make a second pass to set the marked rows and columns to 0
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // set the first column to 0 if needed
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
- We use the first row and first column to track which rows and columns need to be set to 0, reducing the need for extra space.
- This solution has a time complexity of O(m * n), where m and n are the dimensions of the input matrix.
- This approach modifies the input matrix in-place, as required by the problem statement.