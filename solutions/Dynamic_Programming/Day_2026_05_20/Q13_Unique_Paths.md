# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has obstacles, but for this problem, there are no obstacles. The robot can move down or right from any cell. For example, for a 3x7 grid, there are 28 unique paths.

## Approach
The problem can be solved by using dynamic programming to store the number of unique paths to each cell. We start by initializing the first row and column to 1, since there is only one way to reach each cell in the first row and column. Then, for each remaining cell, we calculate the number of unique paths as the sum of the number of unique paths to the cell above it and the cell to its left.

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
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first row and column to 1
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        
        // Calculate the number of unique paths to each remaining cell
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // Return the number of unique paths to the bottom-right corner
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
- The problem can be solved using dynamic programming to store the number of unique paths to each cell.
- The time complexity is O(m*n) because we need to iterate over each cell in the grid.
- The space complexity is O(m*n) because we need to store the number of unique paths to each cell in a 2D vector.