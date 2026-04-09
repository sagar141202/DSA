# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, i.e., modify the input matrix directly. The matrix is represented as a 2D array of integers. For example, given the following matrix:
```
[
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
```
The output should be:
```
[
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
```
The constraints are: 1 <= m, n <= 200.

## Approach
The approach involves iterating over the matrix to find the rows and columns that contain a 0, then modifying those rows and columns to be all 0s. We use two sets to keep track of the rows and columns to be modified.

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

    // Find the rows and cols that need to be zeroed
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i] = true;
                cols[j] = true;
            }
        }
    }

    // Zero out the rows and cols
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (rows[i] || cols[j]) {
                matrix[i][j] = 0;
            }
        }
    }
}

int main() {
    vector<vector<int>> matrix = {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1}
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
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
Output: 
[
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
]
```

## Key Takeaways
- We can use two separate vectors to keep track of the rows and columns that need to be zeroed.
- The solution has a time complexity of O(m * n) where m and n are the dimensions of the matrix.
- The space complexity is O(m + n) due to the two vectors used to keep track of the rows and columns.