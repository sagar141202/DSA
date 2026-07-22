# Maximum Square of 1s

## Problem Statement
Given a binary matrix (2D array) filled with 0s and 1s, find the size of the largest square submatrix that contains all 1s. The size of the square submatrix is defined as the length of its side. For example, given the following binary matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
The largest square submatrix that contains all 1s has a size of 3.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the size of the largest square submatrix with its bottom right corner at `(i, j)`. We iterate over the matrix and update `dp[i][j]` based on the values of `dp[i-1][j]`, `dp[i][j-1]`, and `dp[i-1][j-1]`.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        int maxSide = 0;
        
        // Initialize the first row and column
        for (int i = 0; i < m; i++) {
            dp[i][0] = matrix[i][0] - '0';
            maxSide = max(maxSide, dp[i][0]);
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = matrix[0][j] - '0';
            maxSide = max(maxSide, dp[0][j]);
        }
        
        // Fill the rest of the dp table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == '1') {
                    dp[i][j] = min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1])) + 1;
                    maxSide = max(maxSide, dp[i][j]);
                }
            }
        }
        
        return maxSide * maxSide;
    }
};
```

## Test Cases
```
Input: 
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 4

Input: 
[
  ["0"]
]
Output: 0
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the size of the largest square submatrix with its bottom right corner at `(i, j)`.
- The time complexity of the solution is O(m*n) where m and n are the dimensions of the input matrix.
- The space complexity of the solution is also O(m*n) as we need to store the `dp` table.