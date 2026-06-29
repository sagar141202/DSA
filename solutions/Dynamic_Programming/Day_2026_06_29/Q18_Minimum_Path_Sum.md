# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The input grid will have `m` rows and `n` columns, where each cell contains a non-negative integer. The goal is to find the minimum sum of the numbers in the path from the top left cell to the bottom right cell.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the minimum sum of the path to reach that cell. We start by initializing the first cell with the value of the top left cell in the grid, then fill in the rest of the table row by row.

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
        
        // Initialize the first cell
        for (int i = 1; i < n; i++) {
            grid[0][i] += grid[0][i-1];
        }
        for (int i = 1; i < m; i++) {
            grid[i][0] += grid[i-1][0];
        }
        
        // Fill in the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }
        
        // The minimum sum is stored in the bottom right cell
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
- The dynamic programming approach allows us to avoid redundant calculations by storing the results of subproblems in a table.
- The time complexity is O(mn) because we need to fill in the entire table, where m is the number of rows and n is the number of columns.
- The space complexity is also O(mn) because we need to store the entire table in memory.