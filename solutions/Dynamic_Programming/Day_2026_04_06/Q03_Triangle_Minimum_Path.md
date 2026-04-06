# Triangle Minimum Path

## Problem Statement
Given a triangle array where each element represents the cost of reaching that cell, find the minimum cost path from the top to the bottom. The path can only be either directly down or diagonally down to the left or right. The triangle array is represented as a 2D vector where each sub-vector represents a row in the triangle. For example, `[[2], [3,4], [6,5,7], [4,1,8,3]]` represents the following triangle:
```
    2
   3 4
  6 5 7
 4 1 8 3
```
The minimum cost path is the path with the minimum sum of costs. For example, in the given triangle, the minimum cost path is `2 + 3 + 5 + 1 = 11`.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the minimum cost to reach the cell at position `(i, j)`. We fill up the `dp` array row by row, starting from the top.

## Complexity
- Time: O(n^2)
- Space: O(n^2)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        vector<vector<int>> dp(n);
        for (int i = 0; i < n; i++) {
            dp[i].resize(triangle[i].size());
        }
        
        // Initialize the first row
        dp[0][0] = triangle[0][0];
        
        // Fill up the dp array row by row
        for (int i = 1; i < n; i++) {
            dp[i][0] = dp[i-1][0] + triangle[i][0];
            for (int j = 1; j < triangle[i].size() - 1; j++) {
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j];
            }
            dp[i][triangle[i].size() - 1] = dp[i-1][triangle[i-1].size() - 1] + triangle[i][triangle[i].size() - 1];
        }
        
        // Find the minimum cost in the last row
        int minCost = INT_MAX;
        for (int j = 0; j < triangle[n-1].size(); j++) {
            minCost = min(minCost, dp[n-1][j]);
        }
        
        return minCost;
    }
};
```

## Test Cases
```
Input: [[2], [3,4], [6,5,7], [4,1,8,3]]
Output: 11
```

## Key Takeaways
- The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the minimum cost to reach the cell at position `(i, j)`.
- The `dp` array is filled up row by row, starting from the top.
- The minimum cost path is the path with the minimum sum of costs, which can be found by iterating over the last row of the `dp` array.