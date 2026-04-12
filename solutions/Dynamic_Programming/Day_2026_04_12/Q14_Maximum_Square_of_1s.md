# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area. The matrix has dimensions m x n, where m and n are integers between 1 and 200. Each cell in the matrix contains either 0 or 1. For example, given the following matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
The largest square of 1s has an area of 4.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D table where each cell represents the size of the largest square with its bottom right corner at that cell. The size of the square at each cell is determined by the minimum size of the squares above, to the left, and to the top-left, plus one.

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
            dp[i][0] = matrix[i][0] - '0';
            maxSide = max(maxSide, dp[i][0]);
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = matrix[0][j] - '0';
            maxSide = max(maxSide, dp[0][j]);
        }
        
        // Fill up the rest of the table
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
  ["1","0","0","1","0"]
]
Output: 4
```

## Key Takeaways
- The dynamic programming table `dp` is used to store the size of the largest square with its bottom right corner at each cell.
- The size of the square at each cell is determined by the minimum size of the squares above, to the left, and to the top-left, plus one.
- The maximum side length of the square is updated throughout the process to finally return the area of the largest square.