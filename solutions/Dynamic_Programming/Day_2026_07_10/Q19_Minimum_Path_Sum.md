# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum is `1 + 3 + 1 + 1 + 1 = 7`.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the minimum path sum to reach the cell at position `(i, j)`. We fill up the `dp` array row by row, and for each cell, we choose the minimum path sum from the cell above it or to its left, and add the value of the current cell.

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
        
        // Fill up the first row
        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }
        
        // Fill up the first column
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        
        // Fill up the rest of the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        
        return dp[m-1][n-1];
    }
};
```

## Test Cases
```
Input: [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7

Input: [
  [1,2,3],
  [4,5,6]
]
Output: 12
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant calculations and reduce the time complexity to O(m*n).
- The space complexity can be optimized to O(n) by only keeping the previous row in the `dp` array.
- The problem can be extended to allow diagonal movements, which would require a different approach.