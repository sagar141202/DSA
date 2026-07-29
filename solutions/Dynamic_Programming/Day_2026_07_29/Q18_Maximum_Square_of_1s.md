# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0s and 1s, find the largest square containing only 1s and return its area. The matrix has dimensions `m x n`, where `m` and `n` are integers between 1 and 200. Each cell in the matrix contains either 0 or 1. The function should return the area of the largest square of 1s.

## Approach
The approach to solve this problem involves using dynamic programming to build a table where each cell represents the size of the largest square of 1s with its bottom right corner at that cell. We then iterate over the table to find the maximum size.

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
        
        // Fill the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == '1') {
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
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

Input: 
[
  ["0","0"]
]
Output: 0
```

## Key Takeaways
- We use dynamic programming to solve this problem efficiently by avoiding redundant computations.
- The `dp` table is used to store the size of the largest square of 1s with its bottom right corner at each cell.
- The maximum size of the square is updated as we fill the `dp` table.