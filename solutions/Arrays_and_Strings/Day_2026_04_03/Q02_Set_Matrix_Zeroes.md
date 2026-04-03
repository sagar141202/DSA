# Set Matrix Zeroes

## Problem Statement
Given an `m x n` matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you should not use any extra space that scales with the input size. The input matrix is represented as a 2D vector of integers. For example, given the following matrix:
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
The constraints are: `m == matrix.length`, `n == matrix[0].length`, `1 <= m, n <= 200`, and `0 <= matrix[i][j] <= 231 - 1`.

## Approach
The approach is to use the first row and first column to track which rows and columns need to be zeroed out. We iterate over the matrix to find the zeros, then use the first row and column to mark the corresponding rows and columns. Finally, we iterate over the matrix again to set the marked rows and columns to zero.

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
        if (matrix[i][0] == 0) isCol = true;
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

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

    for (auto row : matrix) {
        for (int val : row) {
            cout << val << " ";
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
- We can use the first row and first column to track which rows and columns need to be zeroed out.
- We need to handle the first row and first column separately to avoid overwriting the tracking information.
- The solution has a time complexity of O(m * n) and a space complexity of O(1), where m is the number of rows and n is the number of columns in the matrix.