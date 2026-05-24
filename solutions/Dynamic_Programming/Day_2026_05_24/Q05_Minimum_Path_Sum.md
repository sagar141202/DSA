# Minimum Path Sum

## Problem Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right, not diagonally. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum from top left to bottom right is `1 + 3 + 1 + 1 + 1 = 7` and `1 + 1 + 1 + 2 + 1 = 6` are two possible paths with the minimum sum being 7.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table in a bottom-up manner. We start from the first cell and fill up the table based on the minimum sum of the cell above it and the cell to its left. The minimum path sum is stored in the last cell of the table.

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
        
        // Fill up the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }
        
        // The minimum path sum is stored in the last cell
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
- We can solve this problem using dynamic programming by building a 2D table in a bottom-up manner.
- The time complexity is O(m*n) where m and n are the dimensions of the grid.
- The space complexity is O(m*n) as we need to store the 2D table.