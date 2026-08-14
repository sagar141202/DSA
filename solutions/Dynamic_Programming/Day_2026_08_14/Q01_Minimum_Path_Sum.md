# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The input grid will have `m` rows and `n` columns, and all elements will be non-negative integers. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum is `1 + 3 + 1 + 1 + 1 = 7`, which can be achieved by moving right, then down, then down, then right.

## Approach
We will use dynamic programming to solve this problem by building a 2D table where each cell represents the minimum path sum to reach that cell. The algorithm will fill up this table row by row, considering the minimum sum of the cell above and the cell to the left.

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
        
        // Fill up the rest of the table
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
- The dynamic programming approach allows us to break down the problem into smaller subproblems and store their solutions to avoid redundant computation.
- The time complexity is O(m*n) because we need to fill up the entire table, and the space complexity is also O(m*n) because we need to store the entire table.
- The solution can be further optimized by using a 1D array instead of a 2D array to store the minimum path sums, since each cell only depends on the cell above and the cell to the left.