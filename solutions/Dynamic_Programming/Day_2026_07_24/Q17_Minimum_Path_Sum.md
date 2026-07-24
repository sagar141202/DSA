# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The grid is represented by a 2D array `grid` where `grid[i][j]` is the value at the cell at the `i`-th row and `j`-th column. The path must start at `grid[0][0]` and end at `grid[m-1][n-1]`. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum is `1 + 3 + 1 + 1 + 1 = 7`, which can be achieved by going down, then right, then down, then right.

## Approach
We will use dynamic programming to solve this problem, building up a solution by computing the minimum path sum to each cell. The minimum path sum to a cell is the minimum of the path sums to the cell above it and the cell to its left, plus the value of the current cell. We can fill in the `grid` in a bottom-up manner to compute the minimum path sum.

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
        
        // Fill in the rest of the grid
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
- To solve this problem, we need to use dynamic programming to build up the minimum path sum to each cell.
- The minimum path sum to a cell is the minimum of the path sums to the cell above it and the cell to its left, plus the value of the current cell.
- We can fill in the `grid` in a bottom-up manner to compute the minimum path sum.