# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0s and 1s, find the largest square containing only 1s and return its area. The matrix can have dimensions up to 200x200, and each cell can be either 0 or 1. For example, given the matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 1 1 1 0
```
The largest square of 1s has an area of 9 (3x3 square of 1s in the middle).

## Approach
This problem can be solved using dynamic programming, where we build a table in a bottom-up manner, storing the size of the largest square that can be formed at each position. The size of the square at each cell is determined by the minimum size of the squares above, to the left, and to the top-left, plus one.

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
        if (matrix.empty() || matrix[0].empty()) return 0;
        
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
  ["1","1","1","1","0"]
]
Output: 4
```

## Key Takeaways
- To solve this problem, we need to understand how to apply dynamic programming to build a table that stores the size of the largest square at each position.
- We initialize the first row and column of the table based on the input matrix, and then fill up the rest of the table using the minimum size of the squares above, to the left, and to the top-left, plus one.
- The final answer is the square of the maximum side length found in the table.