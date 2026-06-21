# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0s and 1s, find the largest square containing all 1s and return its area. The matrix can be of any size, but it will not be empty. For example, given the following matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 1 1 1 0
```
The largest square of 1s has an area of 4.

## Approach
The solution uses dynamic programming to build a table where each cell represents the size of the largest square of 1s ending at that cell. The algorithm iterates through the matrix, updating the table based on the values of the current cell and its neighbors.

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
        
        // Fill the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == '1') {
                    dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1;
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
Input: 
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","1","1","1","0"]
]
Output: 4
```

## Key Takeaways
- The dynamic programming approach allows for efficient computation of the largest square of 1s by breaking down the problem into smaller sub-problems.
- The `dp` table is used to store the size of the largest square of 1s ending at each cell, which helps to avoid redundant computations.
- The time complexity of the solution is O(m*n), where m and n are the dimensions of the input matrix.