# Set Matrix Zeroes

## Problem Statement
Given a matrix, if an element is 0, set its entire row and column to 0. The matrix is modified in-place. The constraints are: 1 <= matrix.length <= 200, 1 <= matrix[0].length <= 200, and -10^9 <= matrix[i][j] <= 10^9. For example, given the matrix [[1,1,1],[1,0,1],[1,1,1]], the output should be [[1,0,1],[0,0,0],[1,0,1]].

## Approach
We will use two sets to keep track of the rows and columns that need to be zeroed. We iterate over the matrix to find the zeros and store the corresponding row and column indices. Then, we iterate over the matrix again to set the zeros.

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
    vector<int> rows(m, 0);
    vector<int> cols(n, 0);

    // Find the zeros
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 0) {
                rows[i] = 1;
                cols[j] = 1;
            }
        }
    }

    // Set the zeros
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
Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Input: [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```

## Key Takeaways
- Use two separate vectors to track the rows and columns that need to be zeroed.
- Perform two passes over the matrix: one to find the zeros and another to set the zeros.
- Use a space complexity of O(m + n) to store the row and column indices.