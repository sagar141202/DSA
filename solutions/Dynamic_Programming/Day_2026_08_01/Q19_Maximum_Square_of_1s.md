# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0s and 1s, find the largest square containing all 1s and return its area. The matrix can be of any size, but it will always be a square matrix (i.e., have the same number of rows and columns). For example, given the following matrix:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
The largest square of 1s has an area of 4 (the 2x2 square in the bottom left corner), but since we can find a larger square of size 3x3 in the given matrix, the answer would be 9.

## Approach
The approach to solve this problem involves using dynamic programming to build a table where each cell contains the size of the largest square of 1s that can be formed with the current cell as the bottom right corner. We then find the maximum value in this table, which represents the size of the largest square of 1s in the matrix.

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
        
        // Fill the rest of the table
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == '1') {
                    dp[i][j] = min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]}) + 1;
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

Input: 
[
  ["0"]
]
Output: 0

Input: 
[
  ["0","0"]
]
Output: 0
```

## Key Takeaways
- We can use dynamic programming to solve this problem efficiently by building a table that stores the size of the largest square of 1s that can be formed at each position.
- The size of the largest square of 1s that can be formed at each position is determined by the minimum size of the squares above, to the left, and to the top-left, plus one.
- The area of the largest square is the square of its side length, which can be found by taking the maximum value in the table and squaring it.