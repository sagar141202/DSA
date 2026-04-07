# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0s and 1s, find the largest square containing all 1s and return its area. The matrix can contain up to 200 rows and 200 columns, with each element being either 0 or 1. For example, given the following matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
The largest square of 1s has an area of 4.

## Approach
We can solve this problem using dynamic programming by maintaining a table where each cell represents the size of the largest square ending at that cell. We iterate over the matrix, updating the table based on the values of the current cell and its neighbors. The maximum size of a square found during the iteration is the answer.

## Complexity
- Time: O(m*n)
- Space: O(m*n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        
        // Create a table to store the size of the largest square ending at each cell
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        int maxSide = 0;
        
        // Initialize the first row and column of the table
        for (int i = 0; i < m; i++) {
            dp[i][0] = matrix[i][0] - '0';
            maxSide = max(maxSide, dp[i][0]);
        }
        
        for (int j = 0; j < n; j++) {
            dp[0][j] = matrix[0][j] - '0';
            maxSide = max(maxSide, dp[0][j]);
        }
        
        // Fill the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == '1') {
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
                    maxSide = max(maxSide, dp[i][j]);
                }
            }
        }
        
        // The area of the largest square is the square of its side length
        return maxSide * maxSide;
    }
};
```

## Test Cases
```
Input: 
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 4
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems and optimal substructure.
- The size of the largest square ending at each cell can be calculated based on the values of the current cell and its neighbors.
- The maximum size of a square found during the iteration is the answer.