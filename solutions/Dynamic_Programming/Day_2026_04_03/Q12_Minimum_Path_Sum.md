# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The grid is represented as a 2D array `grid` where `grid[i][j]` represents the value at position `(i, j)`. The path must start from the top left corner `grid[0][0]` and end at the bottom right corner `grid[m-1][n-1]`.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the minimum sum of the path from the top left corner to the cell at `(i, j)`. We fill up the `dp` array row by row from left to right and top to bottom.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first cell
        dp[0][0] = grid[0][0];
        
        // Fill the first row
        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }
        
        // Fill the first column
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        
        // Fill the rest of the cells
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
            }
        }
        
        return dp[m-1][n-1];
    }
};
```

## Test Cases
```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Path with minimum sum: 1 -> 3 -> 1 -> 1 -> 1
```

## Key Takeaways
- The dynamic programming approach helps to avoid redundant calculations and reduce the time complexity.
- The `dp` array is used to store the minimum sum of the path to each cell, which helps to make the decision for the next cell.
- The problem can be solved by filling up the `dp` array row by row from left to right and top to bottom.