# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The grid is represented as a 2D array of integers, where `grid[i][j]` represents the value at position `(i, j)`. The path sum is the sum of all values in the path.

## Approach
We will use dynamic programming to solve this problem by building a 2D table where each cell represents the minimum path sum to reach that cell. We will fill the table row by row, using the minimum sum of the cell above and to the left of the current cell.

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
        
        // Initialize the first row
        for (int i = 1; i < m; i++) {
            grid[i][0] += grid[i-1][0];
        }
        
        // Fill the rest of the table
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
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
```

## Key Takeaways
- The dynamic programming approach is useful for solving problems that have overlapping subproblems.
- The time complexity of this solution is O(m*n) because we need to fill the entire table.
- The space complexity of this solution is O(m*n) because we need to store the entire table.