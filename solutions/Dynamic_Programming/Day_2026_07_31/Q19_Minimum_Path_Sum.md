# Minimum Path Sum

## Problem Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum is 7, which is achieved by the path 1 -> 3 -> 1 -> 1 -> 1.

## Approach
The problem can be solved using Dynamic Programming by maintaining a 2D array `dp` where `dp[i][j]` represents the minimum path sum to reach the cell at position `(i, j)`. We can fill up this array by iterating over the grid and at each cell, choosing the minimum path sum from the top or left cell.

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
        // Create a 2D array to store the minimum path sum to reach each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first cell with the value of the top-left cell in the grid
        dp[0][0] = grid[0][0];
        
        // Fill up the first row
        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }
        
        // Fill up the first column
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        
        // Fill up the rest of the array
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
            }
        }
        
        // The minimum path sum is stored in the bottom-right cell of the array
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
- The problem can be solved using Dynamic Programming with a time complexity of O(m*n) and space complexity of O(m*n).
- We need to initialize the first row and column of the `dp` array separately before filling up the rest of the array.
- The minimum path sum is achieved by choosing the minimum path sum from the top or left cell at each position.