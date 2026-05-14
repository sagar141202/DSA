# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you cannot use any additional space that scales with the input size, other than a constant amount of space. The matrix is represented by a 2D vector of integers. The input matrix will have at least one row and one column, and all elements will be integers between 0 and 100. For example, given the following matrix: 
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

## Approach
The approach involves using the first row and first column of the matrix as flags to track which rows and columns need to be set to zero. We iterate over the matrix to find the zeros, then use the flags to set the corresponding rows and columns to zero.

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
    bool isCol = false;

    // Iterate over the matrix to find the zeros
    for (int i = 0; i < m; i++) {
        // Check if the first column needs to be set to zero
        if (matrix[i][0] == 0) {
            isCol = true;
        }
        // Check the rest of the columns
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                // Use the first row and first column as flags
                matrix[0][j] = 0;
                matrix[i][0] = 0;
            }
        }
    }

    // Set the rows and columns to zero based on the flags
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Set the first row to zero if necessary
    if (matrix[0][0] == 0) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }

    // Set the first column to zero if necessary
    if (isCol) {
        for (int i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
}

int main() {
    // Example usage:
    vector<vector<int>> matrix = {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1}
    };
    setZeroes(matrix);
    // Print the result
    for (const auto& row : matrix) {
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
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
```

## Key Takeaways
- We use the first row and first column as flags to track which rows and columns need to be set to zero.
- The time complexity is O(m*n) because we need to iterate over the entire matrix.
- The space complexity is O(1) because we only use a constant amount of space, excluding the space needed for the input and output.