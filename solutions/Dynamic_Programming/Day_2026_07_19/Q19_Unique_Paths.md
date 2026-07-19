# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The robot can only move down or right.

## Approach
This problem can be solved using dynamic programming, where we build up a table of solutions to sub-problems. We initialize a 2D array dp where dp[i][j] represents the number of unique paths to reach the cell at position (i, j). We then fill up the table by iterating over each cell and calculating the number of unique paths to reach that cell.

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
        
        // Fill up the table by iterating over each cell
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to reach a cell is the sum of the number of unique paths to reach the cell above it and the cell to its left
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // The number of unique paths to reach the bottom-right corner is stored in the bottom-right cell of the table
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
- Dynamic programming can be used to solve problems that have overlapping sub-problems.
- The time complexity of dynamic programming solutions is often O(n^2) or O(n^3), where n is the size of the input.
- The space complexity of dynamic programming solutions is often O(n^2) or O(n^3), where n is the size of the input.