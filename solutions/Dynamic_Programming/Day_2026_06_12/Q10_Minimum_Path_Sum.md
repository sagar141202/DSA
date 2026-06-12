# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right, i.e., we can only move either down or right at any point in time. The grid will not be empty and will have at least one row and one column. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum is `7` because the path `1 -> 3 -> 1 -> 1 -> 1` has the minimum sum.

## Approach
We will use dynamic programming to solve this problem, where `dp[i][j]` represents the minimum path sum to reach cell `(i, j)`. We will fill up the `dp` table by iterating over the grid and updating `dp[i][j]` as the minimum of `dp[i-1][j]` and `dp[i][j-1]` plus the current cell value. 

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
        
        // Initialize the first cell
        for (int i = 1; i < m; i++) {
            grid[i][0] += grid[i-1][0];
        }
        for (int j = 1; j < n; j++) {
            grid[0][j] += grid[0][j-1];
        }
        
        // Fill up the rest of the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }
        
        return grid[m-1][n-1];
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
- We can use dynamic programming to solve this problem efficiently by breaking it down into smaller subproblems.
- The `dp` table can be filled up in a bottom-up manner, where each cell depends on the values of its top and left neighbors.
- The minimum path sum can be found by returning the value of the bottom-right cell in the `dp` table.