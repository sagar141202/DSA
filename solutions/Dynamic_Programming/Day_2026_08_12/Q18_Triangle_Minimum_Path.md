# Triangle Minimum Path

## Problem Statement
Given a triangle, find the minimum path sum from top to bottom. Each step, you may move to either the number directly below the current number or the number directly below and to the right of the current number. The triangle is represented as a 2D array where each sub-array represents a row in the triangle. For example, given the triangle `[[2], [3,4], [6,5,7], [4,1,8,3]]`, the minimum path sum is `11` (i.e., `2 + 3 + 5 + 1 = 11`).

## Approach
We will use dynamic programming to solve this problem, starting from the bottom of the triangle and working our way up. At each step, we calculate the minimum path sum to each number by considering the minimum path sum to the numbers below it.

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
        // Create a copy of the input triangle to store the minimum path sums
        vector<vector<int>> dp = triangle;
        
        // Start from the second last row and work our way up
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // For each number, calculate the minimum path sum by considering the numbers below it
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
Input: [[2], [3,4], [6,5,7], [4,1,8,3]]
Output: 11
Input: [[-10]]
Output: -10
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping sub-problems.
- The key to solving this problem is to start from the bottom of the triangle and work our way up, calculating the minimum path sum to each number by considering the numbers below it.
- The time complexity of this solution is O(n^2) where n is the number of rows in the triangle, and the space complexity is also O(n^2) as we need to store the minimum path sums for each number in the triangle.