# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The grid is represented as a 2D array of integers, where `grid[i][j]` represents the value at position `(i, j)`. The path can start from the top left corner, and the goal is to reach the bottom right corner with the minimum sum.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table `dp` in a bottom-up manner. Each cell `dp[i][j]` represents the minimum sum of the path from the top left to the current cell. We fill the table by considering the minimum sum of the path to the cell above and the cell to the left, and adding the current cell's value.

## Complexity
- Time: O(mn)
- Space: O(mn)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Create a 2D table to store the minimum sum of the path to each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first cell with the value of the top left cell in the grid
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
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        
        // The minimum sum of the path is stored in the bottom right cell of the table
        return dp[m-1][n-1];
    }
};
```

## Test Cases
```
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
```

## Key Takeaways
- The problem can be solved using dynamic programming with a time complexity of O(mn) and a space complexity of O(mn).
- The key insight is to build a 2D table `dp` where each cell represents the minimum sum of the path to that cell.
- The table is filled in a bottom-up manner by considering the minimum sum of the path to the cell above and the cell to the left, and adding the current cell's value.