# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right, meaning that from any cell, you can only move either down or right.

## Approach
We will use dynamic programming to solve this problem by breaking it down into smaller sub-problems and storing the results of each sub-problem to avoid redundant computation. We'll create a 2D array `dp` where `dp[i][j]` represents the minimum sum of the path from the top left cell to the cell at `(i, j)`.

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
        for (int i = 1; i < n; i++) {
            grid[0][i] += grid[0][i-1];
        }
        for (int i = 1; i < m; i++) {
            grid[i][0] += grid[i-1][0];
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
Input: [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Input: [[1,2,3],[4,5,6]]
Output: 12
```

## Key Takeaways
- Use dynamic programming to break down the problem into smaller sub-problems and store the results to avoid redundant computation.
- Initialize the base cases (first row and first column) before filling up the rest of the grid.
- Use a bottom-up approach to fill up the grid, starting from the top left cell and moving down and right.