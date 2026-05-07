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
The minimum path sum is 7, which is achieved by the path: 1 -> 3 -> 1 -> 1 -> 1.

## Approach
The problem can be solved using dynamic programming, where we build up a 2D table in a bottom-up manner. We start by initializing the first cell with the value of the top-left cell in the grid. Then, for each cell, we calculate the minimum sum by taking the minimum of the sum from the cell above and the cell to the left, and adding the current cell's value.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
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

Input: [
  [1,2,3],
  [4,5,6]
]
Output: 12
```

## Key Takeaways
- We use dynamic programming to break down the problem into smaller sub-problems and store the solutions to these sub-problems to avoid redundant computation.
- The time complexity is O(m*n) because we need to fill up the entire table.
- The space complexity is O(m*n) because we need to store the entire table.