# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0s and 1s, find the largest square containing all 1s and return its area. The matrix can be of any size, and the square can be oriented in any direction (i.e., it can be a square with sides parallel to the axes or rotated by 45 degrees). For example, given the following matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
The largest square of 1s has an area of 4.

## Approach
The algorithm uses dynamic programming to build a table where each cell represents the size of the largest square of 1s ending at that cell. The size of the largest square is then the maximum value in this table. The dynamic programming approach ensures that the solution is efficient and scalable.

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
        
        // Fill up the rest of the table
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
```

## Key Takeaways
- The dynamic programming approach allows us to solve the problem efficiently by avoiding redundant computations.
- The size of the largest square of 1s can be obtained by finding the maximum value in the dynamic programming table.
- The time complexity of the solution is O(m*n), where m and n are the dimensions of the input matrix.