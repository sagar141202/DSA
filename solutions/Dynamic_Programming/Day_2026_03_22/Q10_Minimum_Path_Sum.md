# Minimum Path Sum

## Problem Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The grid is represented as a 2D array of integers, where grid[i][j] represents the value at position (i, j). The path must start at the top left corner (0, 0) and end at the bottom right corner (m-1, n-1). For example, given the following grid: [[1,3,1],[1,5,1],[4,2,1]], the minimum path sum is 7, which is achieved by the path 1 -> 3 -> 1 -> 1 -> 1.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table in a bottom-up manner. We start by initializing the first cell of the table with the value of the first cell in the grid. Then, we fill the table row by row, where each cell represents the minimum sum of the path from the top left to the current cell. We consider two possibilities for each cell: moving down or moving right.

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
        
        // Fill the rest of the table
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
Input: [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Input: [[1,2,3],[4,5,6]]
Output: 12
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize the base cases carefully to ensure the correctness of the solution.
- Consider all possible scenarios when filling the table to avoid missing any potential solutions.