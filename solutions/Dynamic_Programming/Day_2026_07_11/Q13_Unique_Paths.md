# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the same constraints as a standard grid where you can only move right or down. For example, for a 3x7 grid, the number of unique paths is 28.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of unique paths to each cell. We initialize the first row and column to 1, since there is only one way to reach each cell in the first row and column. Then, for each cell, we calculate the number of unique paths as the sum of the number of unique paths to the cell above it and the cell to its left.

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
        // Create a 2D table to store the number of unique paths to each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first row and column to 1
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        
        // Calculate the number of unique paths to each cell
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // Return the number of unique paths to the bottom-right corner
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The time complexity of the solution is O(m * n), where m and n are the dimensions of the grid.
- The space complexity of the solution is O(m * n), where m and n are the dimensions of the grid.