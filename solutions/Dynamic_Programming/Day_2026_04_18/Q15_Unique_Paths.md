# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The robot can only move down or right, and it must start at the top-left corner and end at the bottom-right corner. For example, if the grid is 3x7, there are 28 unique paths.

## Approach
The problem can be solved using dynamic programming, where we build a 2D table to store the number of unique paths to each cell. We start by initializing the first row and column to 1, since there is only one way to reach each cell in the first row and column. Then, we fill in the rest of the table by adding the number of unique paths to the cell above and the cell to the left.

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
        // Create a 2D table to store the number of unique paths to each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first row and column to 1
        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        
        // Fill in the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // The number of unique paths to a cell is the sum of the number of unique paths to the cell above and the cell to the left
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // The number of unique paths to the bottom-right corner is stored in the last cell of the table
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
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The problem can be broken down into smaller subproblems, and the solutions to these subproblems can be stored in a table to avoid redundant computation.
- The time complexity of the solution is O(m*n), where m and n are the dimensions of the grid, and the space complexity is also O(m*n).