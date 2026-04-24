# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum is `7` because the path that achieves this is `1 -> 3 -> 1 -> 1 -> 1`.

## Approach
The algorithm uses dynamic programming to build up a solution by computing the minimum path sum to each cell from the top left. The minimum path sum to each cell is the minimum of the path sum to the cell above it and the cell to its left, plus the value of the current cell.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

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
- The problem can be solved using dynamic programming by building up a solution from smaller sub-problems.
- The time complexity is O(m * n) because we need to visit each cell in the grid once.
- The space complexity is O(m * n) because we need to store the minimum path sum to each cell in the grid.