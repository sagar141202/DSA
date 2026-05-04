# Minimum Path Sum

## Problem Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum from top left to bottom right is `1 + 3 + 1 + 1 + 1 = 7` and `1 + 1 + 1 + 2 + 1 = 6` are two possible paths, but the minimum path sum is `1 + 3 + 1 + 1 + 1 = 7` is not correct, it is `1 + 1 + 1 + 2 + 1 = 6` and `1 + 3 + 1 + 1 + 1 = 7` is not the minimum, the correct minimum path is `1 + 3 + 1 + 1 + 1 = 7` is not correct, it is `1 + 1 + 1 + 2 + 1 = 6`. The constraints are: `m == grid.length`, `n == grid[i].length`, `1 <= m, n <= 200`, `0 <= grid[i][j] <= 6 * 10^4`.

## Approach
The algorithm uses dynamic programming to build up a solution by computing the minimum sum of all numbers along the path to each cell. The minimum sum to each cell is the minimum of the sum from the cell above it and the cell to its left, plus the value of the current cell. This process is repeated for all cells in the grid.

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
        
        // initialize the first cell
        for (int i = 1; i < m; i++) {
            grid[i][0] += grid[i - 1][0];
        }
        for (int j = 1; j < n; j++) {
            grid[0][j] += grid[0][j - 1];
        }
        
        // fill in the rest of the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1]);
            }
        }
        
        return grid[m - 1][n - 1];
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The time complexity of this solution is O(m * n) because we need to fill in the entire grid.
- The space complexity of this solution is O(1) if we modify the input grid in-place, or O(m * n) if we create a separate grid to store the results.