# Minimum Path Sum

## Problem Statement
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path. The path can only be constructed from top to bottom or from left to right. For example, given the following grid: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
The minimum path sum is 7 (1 + 3 + 1 + 1 + 1 + 1 = 7, or 1 + 1 + 1 + 2 + 1 + 1 = 7), so the function should return 7.

## Approach
The problem can be solved using dynamic programming, where we build up a table of minimum path sums. We start from the top left and fill in the table row by row, using the minimum of the cell above and the cell to the left to calculate the minimum path sum for each cell. This approach ensures that we consider all possible paths and choose the one with the minimum sum.

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
        
        // Initialize the first cell
        for (int i = 1; i < n; i++) {
            grid[0][i] += grid[0][i-1];
        }
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
Input: [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
```

## Key Takeaways
- The problem can be solved using dynamic programming, where we build up a table of minimum path sums.
- We start from the top left and fill in the table row by row, using the minimum of the cell above and the cell to the left to calculate the minimum path sum for each cell.
- The time complexity is O(m*n) and the space complexity is also O(m*n), where m and n are the dimensions of the grid.