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
The minimum path sum from top left to bottom right is `1 + 3 + 1 + 1 + 1 = 7` and `1 + 1 + 1 + 2 + 1 = 6` are two possible paths with the minimum sum of 7 and the other path with sum 6 is `1 + 1 + 1 + 2 + 1`, but there is another path with sum 7, so the minimum sum is 7.

## Approach
We use dynamic programming to solve this problem by initializing the first element of the first row and first column, then filling up the rest of the grid based on the minimum sum of the cell above or to the left. The minimum path sum is stored in the bottom right cell of the grid.

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

        // Initialize the first element of the first row and first column
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

        // The minimum path sum is stored in the bottom right cell of the grid
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
- The dynamic programming approach can be used to solve this problem by breaking it down into smaller sub-problems.
- The time complexity of this solution is O(m*n) where m is the number of rows and n is the number of columns in the grid.
- The space complexity of this solution is also O(m*n) as we are modifying the input grid in-place.