# Set Matrix Zeroes

## Problem Statement
Given an m x n matrix, if an element is 0, set its entire row and column to 0. Do this in-place, meaning you should not use any extra space that scales with the size of the input. The matrix is modified in-place, and you do not need to return anything. However, for the purpose of this exercise, we will return the modified matrix. The input matrix will contain only integers (0 or non-zero).

## Approach
We can solve this problem by using the first row and first column to track the rows and columns that need to be set to zero. We iterate over the matrix to find the zeros and mark the corresponding rows and columns. Then, we iterate over the matrix again to set the marked rows and columns to zero.

## Complexity
- Time: O(m * n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        // Use the first row and first column to track the rows and columns that need to be set to zero
        bool firstRowZero = false;
        bool firstColZero = false;
        
        // Iterate over the matrix to find the zeros and mark the corresponding rows and columns
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) firstColZero = true;
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    if (i == 0) firstRowZero = true;
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        // Iterate over the matrix again to set the marked rows and columns to zero
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        // Set the first row and first column to zero if necessary
        if (firstRowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
};

int main() {
    Solution solution;
    vector<vector<int>> matrix = {{1, 1, 1}, {1, 0, 1}, {1, 1, 1}};
    solution.setZeroes(matrix);
    for (auto row : matrix) {
        for (auto num : row) {
            cout << num << " ";
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
- Use the first row and first column to track the rows and columns that need to be set to zero.
- Iterate over the matrix twice to find the zeros and set the marked rows and columns to zero.
- Handle the first row and first column separately to avoid overwriting the tracking information.