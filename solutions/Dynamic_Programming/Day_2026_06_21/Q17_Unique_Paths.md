# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The robot can start at any cell, but it must end at the bottom-right corner. For example, given m = 3 and n = 7, there are 28 possible unique paths from the top-left corner to the bottom-right corner.

## Approach
We will use dynamic programming to solve this problem by breaking it down into smaller subproblems and storing the results of these subproblems to avoid redundant computation. The idea is to build a 2D table where each cell represents the number of unique paths to reach that cell. We can move to a cell from the cell above it or to its left.

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
        // Create a 2D table to store the number of unique paths to each cell
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        // Fill the table in a bottom-up manner
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and to its left
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // The number of unique paths to the bottom-right corner is stored in the bottom-right cell of the table
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
- The problem can be solved using dynamic programming by breaking it down into smaller subproblems and storing the results of these subproblems.
- The time complexity of the solution is O(m * n), where m and n are the dimensions of the grid.
- The space complexity of the solution is O(m * n), which is used to store the 2D table.