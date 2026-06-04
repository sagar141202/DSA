# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do not return anything, but modify the matrix in-place. The matrix will contain only integers (0s and 1s). The input matrix will have at most 200 rows and columns, and the values will be in the range [0, 1]. For example, given the following matrix: 
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
The algorithm uses two arrays to track the rows and columns that need to be zeroed. It iterates over the matrix to find the zeros, then iterates again to set the corresponding rows and columns to zero. This approach ensures that the matrix is modified in-place.

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

    // Find the rows and columns that need to be zeroed
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i] = true;
                cols[j] = true;
            }
        }
    }

    // Set the corresponding rows and columns to zero
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
    // Print the modified matrix
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
```

## Key Takeaways
- Use two arrays to track the rows and columns that need to be zeroed to avoid modifying the matrix prematurely.
- Iterate over the matrix twice: once to find the zeros and once to set the corresponding rows and columns to zero.
- This approach ensures that the matrix is modified in-place as required by the problem statement.