# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The grid is represented as a 2D array `grid` where `grid[i][j]` represents the value at the cell `(i, j)`. The constraints are `1 <= m <= 100`, `1 <= n <= 100`, and `0 <= grid[i][j] <= 100`. For example, given the grid `[[1,3,1],[1,5,1],[4,2,1]]`, the minimum path sum is `7` because the path `1 -> 3 -> 1 -> 1 -> 1` has the minimum sum.

## Approach
The algorithm uses dynamic programming to build up a solution by computing the minimum path sum to each cell from the top left. It iterates over each cell in the grid, updating the minimum path sum to that cell based on the minimum path sums of the cells above and to the left. The final minimum path sum is stored in the bottom right cell.

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
        
        // Fill in the rest of the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }
        
        // The minimum path sum is stored in the bottom right cell
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The minimum path sum to a cell can be computed by considering the minimum path sums of the cells above and to the left.
- The time and space complexity of the solution are O(m*n) due to the need to fill in the entire grid.