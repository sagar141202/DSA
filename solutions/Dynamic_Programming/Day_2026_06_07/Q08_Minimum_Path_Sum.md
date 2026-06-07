# Minimum Path Sum

## Problem Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right, and you cannot go diagonally. For example, given the following grid: [[1,3,1],[1,5,1],[4,2,1]], the minimum path sum is 7, which is achieved by the path 1 -> 3 -> 1 -> 1 -> 1.

## Approach
We will use dynamic programming to solve this problem, building up a table where each cell represents the minimum path sum to reach that cell. We start by initializing the first row and column, then fill in the rest of the table based on the minimum sum of the cell above and to the left.

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
        
        // The minimum path sum is stored in the bottom right cell
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
- The minimum path sum can be computed using dynamic programming by building up a table where each cell represents the minimum path sum to reach that cell.
- The time complexity is O(m*n) because we need to fill in the entire table.
- The space complexity is O(m*n) because we need to store the entire table.