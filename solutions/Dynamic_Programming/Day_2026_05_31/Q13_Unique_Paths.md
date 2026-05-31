# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The robot can only move down or right, and it must start at the top-left corner and end at the bottom-right corner.

## Approach
The problem can be solved using dynamic programming by creating a 2D array dp where dp[i][j] represents the number of unique paths to reach the cell at position (i, j). The algorithm fills up the dp array in a bottom-up manner, starting from the base cases where there is only one way to reach the cells in the first row and first column.

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
        
        // Fill up the dp array in a bottom-up manner
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to reach a cell is the sum of the number of unique paths to reach the cell above it and the cell to its left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        
        // The number of unique paths to reach the bottom-right corner is stored in the last cell of the dp array
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
Input: m = 7, n = 3
Output: 28
Input: m = 3, n = 3
Output: 6
```

## Key Takeaways
- The problem can be solved using dynamic programming by creating a 2D array to store the number of unique paths to each cell.
- The algorithm fills up the dp array in a bottom-up manner, starting from the base cases where there is only one way to reach the cells in the first row and first column.
- The time complexity of the solution is O(m * n) and the space complexity is also O(m * n).