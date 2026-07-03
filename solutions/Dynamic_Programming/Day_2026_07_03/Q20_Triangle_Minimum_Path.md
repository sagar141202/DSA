# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. The triangle array is represented as a 2D array, where each sub-array represents a level in the triangle. For example, given the triangle `[[2], [3,4], [6,5,7], [4,1,8,3]]`, the minimum path sum is `2 + 3 + 5 + 1 = 11`. The constraints are that the input triangle will have at least one row and at most 200 rows, and each row will have at least one element and at most 200 elements.

## Approach
The approach to solve this problem is to use dynamic programming, where we start from the second last row and update each element to be the minimum sum it can produce. We iterate through each row from the second last to the first, updating the elements based on the minimum sum of the two elements directly below it. This way, when we reach the top, we will have the minimum path sum.

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
        
        // Iterate through each row from the second last to the first
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update each element to be the minimum sum it can produce
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum is stored at the top of the dp triangle
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
- The dynamic programming approach allows us to avoid redundant calculations by storing the results of sub-problems in a table.
- The time complexity is O(n^2) because we are iterating through each element in the triangle once.
- The space complexity is O(n^2) because we are creating a copy of the input triangle to store the minimum path sums.