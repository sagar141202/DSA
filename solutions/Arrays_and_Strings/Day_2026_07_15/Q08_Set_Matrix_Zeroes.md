# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place. The matrix is modified in-place, and no extra space can be used other than a constant amount of space for variables. The input matrix is a 2D vector of integers. For example, given the following matrix: 
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

## Approach
The approach is to use the first row and first column to track which rows and columns need to be zeroed. We iterate over the matrix to find the zeros and mark the corresponding rows and columns. Then, we iterate over the matrix again to set the marked rows and columns to zero.

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
        // Check if the first column needs to be zeroed
        if (matrix[i][0] == 0) {
            isCol = true;
        }
        // Mark the rows and columns that need to be zeroed
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
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

int main() {
    vector<vector<int>> matrix = {
        {1,1,1},
        {1,0,1},
        {1,1,1}
    };
    setZeroes(matrix);
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
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
- The first row and first column can be used to track which rows and columns need to be zeroed.
- We need to handle the first row and first column separately because they are used to track the rows and columns.
- The solution has a time complexity of O(m * n) and a space complexity of O(1), making it efficient for large matrices.