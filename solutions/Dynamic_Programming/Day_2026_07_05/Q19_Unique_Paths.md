# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The robot cannot move outside the grid.

## Approach
The problem can be solved using dynamic programming by building a 2D table where each cell represents the number of unique paths to reach that cell. The algorithm starts by initializing the first row and column of the table, then fills in the rest of the table based on the number of unique paths to reach the cell above and to the left of each cell.

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
        // Create a 2D table to store the number of unique paths to reach each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first row and column of the table
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        
        // Fill in the rest of the table based on the number of unique paths to reach the cell above and to the left of each cell
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // The number of unique paths to reach the bottom-right corner of the grid is stored in the bottom-right cell of the table
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
- The problem can be solved using dynamic programming by building a 2D table where each cell represents the number of unique paths to reach that cell.
- The time complexity of the solution is O(m * n) because we need to fill in the entire table.
- The space complexity of the solution is O(m * n) because we need to store the entire table in memory.