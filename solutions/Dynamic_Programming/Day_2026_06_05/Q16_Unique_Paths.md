# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has the following constraints: 1 <= m, n <= 100. The robot can only move down or right, and it cannot move up or left. For example, if the grid is 3x7, there are 28 possible unique paths.

## Approach
We can solve this problem using dynamic programming by creating a 2D array to store the number of unique paths to each cell. The number of unique paths to a cell is the sum of the number of unique paths to the cell above it and the cell to its left. This approach allows us to avoid redundant calculations and improve efficiency.

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
        // Create a 2D array to store the number of unique paths to each cell
        vector<vector<int>> dp(m, vector<int>(n, 1));
        
        // Fill the 2D array using dynamic programming
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        // The number of unique paths to the bottom-right corner is stored in the last cell
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
- Dynamic programming can be used to solve problems with overlapping subproblems.
- The time complexity of this solution is O(m*n) because we need to fill a 2D array of size m x n.
- The space complexity of this solution is O(m*n) because we need to store a 2D array of size m x n.