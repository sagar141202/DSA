# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level of the triangle, find the minimum path sum from the top to the bottom. Each step you may move to adjacent numbers on the row below. The triangle array is represented as a 2D array where each sub-array is a level of the triangle. For example, `[ [2], [3,4], [6,5,7], [4,1,8,3] ]` represents the following triangle: 
```
    2
   3 4
  6 5 7
 4 1 8 3
```
The minimum path sum is the sum of the numbers in the path from the top to the bottom with the smallest possible sum.

## Approach
The problem can be solved using dynamic programming by maintaining a 2D array `dp` where `dp[i][j]` represents the minimum path sum to reach the `j-th` element in the `i-th` row. We build up the `dp` array from the second last row to the first row.

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
        
        // Initialize the last row of dp
        for (int j = 0; j < triangle[n-1].size(); j++) {
            dp[n-1][j] = triangle[n-1][j];
        }
        
        // Fill up the dp array from the second last row to the first row
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1]);
            }
        }
        
        // The minimum path sum is stored in dp[0][0]
        return dp[0][0];
    }
};
```

## Test Cases
```
Input: [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
```

## Key Takeaways
- Use dynamic programming to solve the problem by maintaining a 2D array `dp` where `dp[i][j]` represents the minimum path sum to reach the `j-th` element in the `i-th` row.
- Initialize the last row of `dp` with the values from the last row of the triangle.
- Fill up the `dp` array from the second last row to the first row by using the minimum of the two adjacent numbers in the row below.