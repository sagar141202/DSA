# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100, and the robot can only move right or down.

## Approach
This problem can be solved using dynamic programming, where each cell in the grid represents the number of unique paths to that cell. The algorithm starts by initializing the first row and column, then fills in the rest of the grid based on the number of unique paths to the cell above and to the left.

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
        // Create a 2D vector to store the number of unique paths to each cell
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        // Fill in the rest of the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to this cell is the sum of the number of unique paths to the cell above and to the left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        
        // The number of unique paths to the bottom-right corner is stored in the bottom-right cell of the grid
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
- The problem can be broken down into smaller sub-problems, where each sub-problem represents the number of unique paths to a cell in the grid.
- The solution uses dynamic programming to store the results of each sub-problem and avoid redundant computation.
- The time and space complexity of the solution are both O(m * n), where m and n are the dimensions of the grid.