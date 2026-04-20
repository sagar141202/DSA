# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The answer can be very large, so return it modulo 10^9 + 7.

## Approach
The problem can be solved using dynamic programming, where each cell in the grid represents the number of unique paths to that cell. We start by initializing the first row and column to 1, since there's only one way to reach each cell in the first row and column. Then, for each remaining cell, the number of unique paths is the sum of the number of unique paths to the cell above it and the cell to its left.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // Initialize a 2D array to store the number of unique paths to each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first row and column to 1
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        
        // Fill in the rest of the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to each cell is the sum of the number of unique paths to the cell above it and the cell to its left
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007;
            }
        }
        
        // The number of unique paths to the bottom-right corner is stored in the bottom-right cell of the grid
        return dp[m-1][n-1];
    }
};
```

## Test Cases
```
Input: m = 3, n = 7
Output: 28
Input: m = 3, n = 2
Output: 3
Input: m = 7, n = 3
Output: 28
Input: m = 3, n = 3
Output: 6
```

## Key Takeaways
- The problem can be solved using dynamic programming, where each cell in the grid represents the number of unique paths to that cell.
- The time complexity is O(m * n), where m and n are the dimensions of the grid.
- The space complexity is O(m * n), where m and n are the dimensions of the grid.