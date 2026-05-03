# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0s and 1s, find the largest square containing all 1s and return its area. The matrix has dimensions m x n, where m and n are between 1 and 200. Each cell contains either 0 or 1. The function should return the area of the largest square of 1s.

## Approach
The approach involves using dynamic programming to build a table where each cell represents the size of the largest square of 1s ending at that cell. The value of each cell is determined by the minimum value of the cell above, the cell to the left, and the cell to the top-left, plus 1.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        int maxSide = 0;
        
        // Initialize the first row and column
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == '1') {
                dp[i][0] = 1;
                maxSide = max(maxSide, dp[i][0]);
            }
        }
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == '1') {
                dp[0][j] = 1;
                maxSide = max(maxSide, dp[0][j]);
            }
        }
        
        // Fill the dp table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == '1') {
                    dp[i][j] = min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1;
                    maxSide = max(maxSide, dp[i][j]);
                }
            }
        }
        
        return maxSide * maxSide;
    }
};
```

## Test Cases
```
Input: [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 4
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the largest square of 1s.
- The use of a 2D table to store the size of the largest square of 1s ending at each cell enables the avoidance of redundant computations.
- The final result is the square of the maximum side length found in the table.