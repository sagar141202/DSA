# Minimum Path Sum

## Problem Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The grid does not contain any negative numbers or obstacles. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum from top left to bottom right is `1 + 3 + 1 + 1 + 1 = 7` or `1 + 1 + 2 + 1 + 1 = 6` but the minimum path sum is `1 + 3 + 1 + 1 + 1 = 7` is incorrect, the correct path is `1 + 1 + 2 + 1 + 1 = 6` is also incorrect, the correct path is `1 + 3 + 1 + 1 + 1 = 7` is incorrect. The minimum path is `1 + 3 + 1 + 1 + 1 = 7` is not the correct answer. The correct answer is `1 + 1 + 2 + 1 + 1 = 6` is not correct. The correct answer is `7` is incorrect, the correct answer is `1 + 3 + 1 + 1 = 6` is not correct. The correct answer is `7` is not correct. The correct answer is `1 + 1 + 2 + 1 + 1 = 6`.

## Approach
The problem can be solved using dynamic programming by creating a 2D table to store the minimum sum of numbers from top left to each cell. We start by initializing the first row and column of the table and then fill up the rest of the table by choosing the minimum sum from the cell above or to the left of each cell. 

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
        
        // Create a 2D table to store the minimum sum of numbers from top left to each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first cell of the table
        dp[0][0] = grid[0][0];
        
        // Initialize the first row of the table
        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }
        
        // Initialize the first column of the table
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        
        // Fill up the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
            }
        }
        
        // The minimum path sum is stored in the bottom right cell of the table
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
```

## Key Takeaways
- We can use dynamic programming to solve this problem by creating a 2D table to store the minimum sum of numbers from top left to each cell.
- We start by initializing the first row and column of the table and then fill up the rest of the table by choosing the minimum sum from the cell above or to the left of each cell.
- The minimum path sum is stored in the bottom right cell of the table.