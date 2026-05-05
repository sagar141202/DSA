# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level of the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number in the row below. The triangle array is represented as a 2D array, where each sub-array represents a level of the triangle. The constraints are: 1 <= triangle.length <= 200, and 1 <= triangle[i].length <= 200. For example, given the triangle `[[2],[3,4],[6,5,7],[4,1,8,3]]`, the minimum path sum is `11`, which is `2 + 3 + 5 + 1`.

## Approach
The approach to solve this problem is to use dynamic programming, where we start from the bottom of the triangle and move upwards, calculating the minimum path sum at each step. We use a bottom-up dynamic programming approach to avoid redundant calculations. The minimum path sum at each position is the minimum of the two positions below it, plus the current value.

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
        // Create a copy of the triangle to store the minimum path sum at each position
        vector<vector<int>> dp = triangle;
        
        // Start from the second last row and move upwards
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Calculate the minimum path sum at each position
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum is stored at the top of the triangle
        return dp[0][0];
    }
};
```

## Test Cases
```
Input: [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Input: [[-10]]
Output: -10
```

## Key Takeaways
- Use dynamic programming to avoid redundant calculations and improve efficiency.
- Start from the bottom of the triangle and move upwards to calculate the minimum path sum.
- The minimum path sum at each position is the minimum of the two positions below it, plus the current value.