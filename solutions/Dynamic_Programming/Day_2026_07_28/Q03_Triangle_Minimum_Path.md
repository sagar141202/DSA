# Triangle Minimum Path

## Problem Statement
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. The triangle is represented as a 2D array where each sub-array represents a row in the triangle. For example, given the following triangle:
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
The minimum path sum is 11 (i.e., 2 + 3 + 5 + 1 = 11). The constraints are: 1 <= triangle.length <= 200, and -10^4 <= triangle[i][j] <= 10^4.

## Approach
The approach is to use dynamic programming to build up a solution from the bottom of the triangle to the top. We start by initializing the last row of the triangle as the minimum path sum to each node in the last row. Then, we iterate up the triangle, updating the minimum path sum to each node based on the minimum path sum to its children.

## Complexity
- Time: O(n^2) where n is the number of rows in the triangle
- Space: O(n) where n is the number of rows in the triangle

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        // Initialize the last row as the minimum path sum
        vector<int> dp = triangle.back();
        // Iterate up the triangle
        for (int i = n - 2; i >= 0; --i) {
            // Update the minimum path sum to each node based on its children
            for (int j = 0; j < triangle[i].size(); ++j) {
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1]);
            }
        }
        // The minimum path sum is stored in the first node of the dp array
        return dp[0];
    }
};
```

## Test Cases
```
Input: [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
```

## Key Takeaways
- We use dynamic programming to build up a solution from the bottom of the triangle to the top.
- We initialize the last row of the triangle as the minimum path sum to each node in the last row.
- We iterate up the triangle, updating the minimum path sum to each node based on the minimum path sum to its children.