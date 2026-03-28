# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0s and 1s, find the largest square containing all 1s and return its area. The matrix has dimensions `m x n`, where `m` and `n` are integers between 1 and 200. Each cell in the matrix can have a value of either 0 or 1. For example, given the following matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 1 1 1 0
```
The largest square of 1s has an area of 9 (3x3 square).

## Approach
We will use dynamic programming to build up a table where each cell contains the size of the largest square of 1s with its bottom right corner at that cell. This approach allows us to efficiently compute the solution by considering each cell's value and the values of its neighbors.

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
        
        // Fill up the rest of the table
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
  ["1","1","1","1","0"]
]
Output: 4

Input: 
[
  ["0"]
]
Output: 0

Input: 
[
  ["0","0"],
  ["0","0"]
]
Output: 0
```

## Key Takeaways
- The dynamic programming approach allows us to break down the problem into smaller sub-problems and store the solutions to sub-problems to avoid redundant computation.
- The `dp` table is used to store the size of the largest square of 1s with its bottom right corner at each cell.
- The final solution is the square of the maximum value in the `dp` table.