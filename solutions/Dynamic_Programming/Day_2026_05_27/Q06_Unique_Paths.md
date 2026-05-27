# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The robot can only move down or right, and it must reach the bottom-right corner.

## Approach
The problem can be solved using dynamic programming by breaking it down into smaller sub-problems and storing the results of each sub-problem. We can use a 2D array to store the number of unique paths to each cell. The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // Create a 2D array to store the number of unique paths to each cell
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        // Fill the 2D array
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        
        // Return the number of unique paths to the bottom-right corner
        return dp[m - 1][n - 1];
    }
};
```

## Test Cases
```
Input: m = 3, n = 7
Output: 28
Input: m = 3, n = 2
Output: 3
```

## Key Takeaways
- The problem can be solved using dynamic programming by breaking it down into smaller sub-problems and storing the results of each sub-problem.
- A 2D array can be used to store the number of unique paths to each cell.
- The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left.