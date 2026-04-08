# Minimum Path Sum

## Problem Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right. The input grid is a 2D vector of integers, and the output should be the minimum sum of the path. For example, given the following grid: [[1,3,1],[1,5,1],[4,2,1]], the minimum path sum is 7, which is achieved by the path 1 -> 3 -> 1 -> 1 -> 1.

## Approach
The problem can be solved using dynamic programming by initializing the first row and column of a 2D table, then filling in the rest of the table based on the minimum sum of the cell above and to the left. This approach ensures that the minimum sum is calculated efficiently.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Initialize the first row
        for (int i = 1; i < n; i++) {
            grid[0][i] += grid[0][i-1];
        }
        
        // Initialize the first column
        for (int i = 1; i < m; i++) {
            grid[i][0] += grid[i-1][0];
        }
        
        // Fill in the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]);
            }
        }
        
        return grid[m-1][n-1];
    }
};
```

## Test Cases
```
Input: [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Input: [[1,2,3],[4,5,6]]
Output: 12
```

## Key Takeaways
- The dynamic programming approach is suitable for problems that can be broken down into smaller subproblems.
- Initializing the base cases (first row and column) is crucial for the dynamic programming approach.
- The time complexity of the solution is O(m*n), where m and n are the number of rows and columns in the grid, respectively.