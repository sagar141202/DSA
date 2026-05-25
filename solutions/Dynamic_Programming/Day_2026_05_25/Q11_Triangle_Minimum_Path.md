# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number. The triangle array is represented as a 2D array, where the i-th row has i + 1 elements. For example, given the triangle `[[2], [3,4], [6,5,7], [4,1,8,3]]`, the minimum path sum is 11 (2 + 3 + 5 + 1). The input triangle will have at least one row and at most 200 rows, and each element in the triangle will be between 0 and 9,999.

## Approach
The algorithm uses dynamic programming to build up the minimum path sum from the bottom of the triangle to the top. It iterates over each level, starting from the second last level, and updates the current level with the minimum sum of the current element and its two adjacent elements in the next level. This process continues until the top of the triangle is reached, where the minimum path sum is stored.

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
        // Create a copy of the triangle to store the minimum path sum
        vector<vector<int>> dp = triangle;
        
        // Iterate over each level, starting from the second last level
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the current level with the minimum sum of the current element and its two adjacent elements in the next level
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
Input: [[2], [3,4], [6,5,7], [4,1,8,3]]
Output: 11
```

## Key Takeaways
- The dynamic programming approach is used to build up the minimum path sum from the bottom of the triangle to the top.
- The time complexity is O(n^2), where n is the number of rows in the triangle, because we need to iterate over each element in the triangle.
- The space complexity is O(n^2) because we need to create a copy of the triangle to store the minimum path sum.