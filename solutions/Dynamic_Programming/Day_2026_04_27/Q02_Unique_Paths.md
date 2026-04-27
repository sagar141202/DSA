# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The robot starts at grid cell (1,1) and tries to reach the cell at (m,n).

## Approach
The problem can be solved using dynamic programming, where each cell stores the number of unique paths to reach that cell. The number of unique paths to reach a cell is the sum of the number of unique paths to reach the cell above it and the cell to its left. The base cases are the first row and the first column, where there is only one way to reach each cell.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // Create a 2D array to store the number of unique paths to reach each cell
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        // Fill the dp array in a bottom-up manner
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to reach a cell is the sum of the number of unique paths to reach the cell above it and the cell to its left
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // The number of unique paths to reach the bottom-right corner is stored in the last cell of the dp array
        return dp[m-1][n-1];
    }
};
```

## Test Cases
```
Input: m = 3, n = 7
Output: 28
Input: m = 3, n = 2
Output: 3
Input: m = 7, n = 3
Output: 28
Input: m = 3, n = 3
Output: 6
```

## Key Takeaways
- The problem can be solved using dynamic programming, where each cell stores the number of unique paths to reach that cell.
- The number of unique paths to reach a cell is the sum of the number of unique paths to reach the cell above it and the cell to its left.
- The base cases are the first row and the first column, where there is only one way to reach each cell.