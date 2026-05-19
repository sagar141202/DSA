# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0s and 1s, find the largest square containing all 1s and return its area. The matrix has dimensions `m x n`, where `m` and `n` are integers. For example, given the matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
The maximum square of 1s has an area of 4.

## Approach
The approach is to use dynamic programming to build a table where each cell represents the size of the largest square of 1s ending at that cell. We iterate over the matrix and update the table based on the values of the neighboring cells. The maximum size of the square is then the maximum value in the table.

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
                    dp[i][j] = min(dp[i-1][j], min(dp[i][j-1], dp[i-1][j-1])) + 1;
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

Input: 
[
  ["0"]
]
Output: 0

Input: 
[
  ["1"]
]
Output: 1
```

## Key Takeaways
- The dynamic programming approach allows us to efficiently solve the problem by avoiding redundant computations.
- The time complexity is O(m*n) because we need to iterate over the entire matrix.
- The space complexity is also O(m*n) because we need to store the dynamic programming table.