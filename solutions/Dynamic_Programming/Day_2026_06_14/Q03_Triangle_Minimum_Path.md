# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level of the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number (i.e., the number directly below and to the left or right of the current number). The triangle array is represented as a 2D vector of integers, where each sub-vector represents a level of the triangle. For example, `[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]` represents the following triangle: 
```
   2
  3 4
 6 5 7
4 1 8 3
```
The minimum path sum from top to bottom is `2 + 3 + 5 + 1 = 11`. The path can only move either down to the left or down to the right.

## Approach
The algorithm uses dynamic programming to build up a solution from the bottom of the triangle to the top, at each step choosing the minimum path sum to the current number. This approach avoids redundant computation by storing the minimum path sum to each number in the triangle. The time complexity is O(n^2), where n is the number of rows in the triangle.

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
        // Create a copy of the triangle to store the minimum path sum to each number
        vector<vector<int>> dp = triangle;
        
        // Start from the second last row and move up
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the minimum path sum to the current number
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum is stored in the top of the triangle
        return dp[0][0];
    }
};
```

## Test Cases
```
Input: [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
Output: 11
```

## Key Takeaways
- Use dynamic programming to avoid redundant computation and improve efficiency.
- Start from the bottom of the triangle and move up to build up the solution.
- Store the minimum path sum to each number in the triangle to avoid redundant computation.