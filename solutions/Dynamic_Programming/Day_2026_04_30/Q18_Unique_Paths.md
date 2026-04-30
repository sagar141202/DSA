# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has no obstacles. The number of rows (m) and columns (n) are given. For example, if the grid is 3x7, there are 28 possible unique paths.

## Approach
The problem can be solved using dynamic programming, where each cell in the grid represents the number of unique paths to that cell. The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left. This is because the robot can only move down or right.

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
        // Create a 2D array to store the number of unique paths to each cell
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        // Fill the dp array in a bottom-up manner
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // The number of unique paths to the bottom-right corner is stored in the last cell of the dp array
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
```

## Key Takeaways
- The problem can be solved using dynamic programming, where each cell in the grid represents the number of unique paths to that cell.
- The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left.
- The time complexity of the solution is O(m*n) and the space complexity is O(m*n), where m and n are the number of rows and columns in the grid respectively.