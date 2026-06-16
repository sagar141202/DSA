# Minimum Path Sum

## Problem Statement
Given a `m x n` grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right, with the constraint that each cell can only be visited once. For example, given the following grid: 
```
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
```
The minimum path sum is `1 + 3 + 1 + 1 + 1 = 7`, and the path is from top left to bottom right, only moving right or down.

## Approach
The problem can be solved using dynamic programming, where we build a table in a bottom-up manner to store the minimum sum at each cell. We start from the top left and fill the table row by row, using the minimum sum of the cell above and to the left to calculate the minimum sum of the current cell.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        // Create a table to store the minimum sum at each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Initialize the first cell
        dp[0][0] = grid[0][0];
        
        // Fill the first row
        for (int i = 1; i < n; i++) {
            dp[0][i] = dp[0][i-1] + grid[0][i];
        }
        
        // Fill the first column
        for (int i = 1; i < m; i++) {
            dp[i][0] = dp[i-1][0] + grid[i][0];
        }
        
        // Fill the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]);
            }
        }
        
        // The minimum path sum is stored in the bottom right cell
        return dp[m-1][n-1];
    }
};
```

## Test Cases
```
Input: [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
```

## Key Takeaways
- The dynamic programming approach allows us to avoid redundant calculations and reduce the time complexity to O(m*n).
- The space complexity can be optimized to O(n) by only storing the current row, but in this solution, we use O(m*n) for simplicity.
- The problem can be generalized to find the minimum path sum in a grid with different constraints, such as allowing diagonal movements.