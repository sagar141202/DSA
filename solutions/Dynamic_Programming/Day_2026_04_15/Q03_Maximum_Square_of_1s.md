# Maximum Square of 1s

## Problem Statement
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area. The matrix can be of size up to 200x200. For example, if the input is:
```
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
The output should be 4, which is the area of the largest square of 1's.

## Approach
The solution involves using dynamic programming to build a table where each cell stores the size of the largest square of 1's that can be formed with the current cell as the bottom right corner. The algorithm iterates over the matrix, updating the table based on the values of the cells above, to the left, and to the top-left of the current cell.

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
                    dp[i][j] = min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]) + 1;
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
- The dynamic programming approach allows us to avoid redundant calculations and solve the problem efficiently.
- The table `dp` stores the size of the largest square of 1's that can be formed with each cell as the bottom right corner.
- The final answer is the square of the maximum value in the `dp` table, which represents the area of the largest square of 1's.