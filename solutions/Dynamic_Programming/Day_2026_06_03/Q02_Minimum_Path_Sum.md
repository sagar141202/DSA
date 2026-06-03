# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The input grid will have `m` rows and `n` columns, where each cell contains a non-negative integer. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum is `1 + 3 + 1 + 1 + 1 = 7`, which is obtained by moving right, then down, then right, then down, then right.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the minimum path sum to reach that cell. We fill the table row by row, using the previously computed values to determine the minimum path sum at each cell. The minimum path sum to reach a cell is the minimum of the path sum to reach the cell above it and the cell to its left, plus the value of the current cell.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

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
    
    // Fill the rest of the table
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
        }
    }
    
    return grid[m-1][n-1];
}
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
- We use dynamic programming to build a 2D table where each cell represents the minimum path sum to reach that cell.
- We fill the table row by row, using the previously computed values to determine the minimum path sum at each cell.
- The time complexity is O(m*n) and the space complexity is O(m*n), where m and n are the number of rows and columns in the grid.