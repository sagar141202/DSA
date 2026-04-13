# Minimum Path Sum

## Problem Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or left to right. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum is 7, which is achieved by the path: 1 -> 3 -> 1 -> 1 -> 1.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the minimum sum to reach that cell. The minimum sum to reach a cell is the minimum sum of the cell above it and the cell to its left, plus the value of the current cell.

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
        
        // Fill the rest of the table
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

Input: [
  [1,2,3],
  [4,5,6]
]
Output: 12
```

## Key Takeaways
- The problem is a classic example of dynamic programming, where we break down the problem into smaller sub-problems and store the solutions to sub-problems to avoid redundant computation.
- The time complexity is O(m*n) because we need to fill up the entire table.
- The space complexity is O(m*n) because we need to store the entire table. However, we can optimize the space complexity to O(n) by only keeping the previous row.