# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has no obstacles. 1 <= m, n <= 100.

## Approach
We will use Dynamic Programming to solve this problem, building up a solution by computing the number of unique paths to each cell. The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // Create a 2D vector to store the number of unique paths to each cell
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        // Fill up the dp table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // The number of unique paths to the bottom-right corner is stored in dp[m-1][n-1]
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
- Dynamic Programming is a powerful technique for solving problems that have overlapping subproblems.
- The key to solving this problem is to recognize that the number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left.
- We can use a 2D vector to store the number of unique paths to each cell, and fill up the vector in a bottom-up manner.