# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. You can only move either down or right at any point in time. The grid is represented as a 2D array, where each cell represents the cost of reaching that cell. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum from the top left to the bottom right is `1 + 3 + 1 + 1 + 1 = 7` or `1 + 1 + 2 + 1 + 1 = 6` or other paths, but the minimum one is `1 + 1 + 1 + 4 + 1 = 8` or `1 + 3 + 2 + 1 = 7`. The minimum path sum is `7`.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the minimum sum of all numbers from the top left to the cell at `(i, j)`. We fill up the `dp` array by iterating over the grid and at each cell, we choose the minimum sum between the cell above it and the cell to its left, and add the current cell's value to it.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Create a 2D array to store the minimum sum at each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first cell
        dp[0][0] = grid[0][0];
        
        // Fill up the first row
        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }
        
        // Fill up the first column
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        
        // Fill up the rest of the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
            }
        }
        
        // The minimum path sum is stored in the bottom right cell
        return dp[m-1][n-1];
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
- We use a 2D array `dp` to store the minimum sum at each cell.
- We initialize the first cell and fill up the first row and column separately.
- We fill up the rest of the grid by choosing the minimum sum between the cell above and the cell to the left, and add the current cell's value to it.