# Unique Paths

## Problem Statement
A robot is located at the top-left corner of a m x n grid. The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid. How many possible unique paths are there? The grid has no obstacles, and the robot cannot move outside the grid. For example, for a 3x7 grid, there are 28 unique paths.

## Approach
We will use dynamic programming to solve this problem by maintaining a 2D array where each cell represents the number of unique paths to reach that cell. The algorithm will iterate over each cell in the grid, updating the number of unique paths based on the number of paths to the cell above and to the left.

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
        
        // Iterate over each cell in the grid
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                // Update the number of unique paths to the current cell
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
- The dynamic programming approach allows us to avoid redundant calculations by storing the results of subproblems in a 2D array.
- The time complexity is O(m*n) because we need to iterate over each cell in the grid once.
- The space complexity is O(m*n) because we need to store the number of unique paths to each cell in the grid.