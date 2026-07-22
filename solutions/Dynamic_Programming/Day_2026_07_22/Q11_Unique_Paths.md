# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The robot can only move down or right, and it must start from the top-left corner and end at the bottom-right corner.

## Approach
We can use dynamic programming to solve this problem by breaking it down into smaller sub-problems. We create a 2D array dp where dp[i][j] represents the number of unique paths from the top-left corner to the cell at (i, j). We fill up this array row by row, using the fact that the number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left.

## Complexity
- Time: O(m * n)
- Space: O(m * n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // Create a 2D array to store the number of unique paths
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        // Fill up the array row by row
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // The number of unique paths to the bottom-right corner is stored in the last cell of the array
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
- We use a 2D array to store the number of unique paths to each cell.
- We fill up the array row by row, using the fact that the number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left.
- The time complexity is O(m * n) and the space complexity is O(m * n), where m and n are the dimensions of the grid.