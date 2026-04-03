# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. The triangle array is represented as a 2D array, where each sub-array is a level in the triangle. For example, given the triangle `[[2],[3,4],[6,5,7],[4,1,8,3]]`, the minimum path sum is `2 + 3 + 5 + 1 = 11`. The constraints are that the input triangle will have at least one row and at most 200 rows, and each row will have at least one element and at most 200 elements.

## Approach
The approach to solve this problem is to use dynamic programming, where we start from the second last row and update each element to be the minimum sum it can produce. We then move up the triangle, updating each element to be the minimum sum it can produce, until we reach the top. This process ensures that we consider all possible paths and choose the one with the minimum sum.

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
        // Create a copy of the input triangle to store the minimum sum at each position
        vector<vector<int>> dp = triangle;
        
        // Start from the second last row and move up
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update each element to be the minimum sum it can produce
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
```

## Key Takeaways
- The dynamic programming approach is suitable for this problem because it allows us to break down the problem into smaller sub-problems and store the results of each sub-problem to avoid redundant computation.
- The time complexity is O(n^2) because we need to iterate over each element in the triangle, and the space complexity is also O(n^2) because we need to store the minimum sum at each position in the triangle.
- The key to solving this problem is to start from the second last row and move up, updating each element to be the minimum sum it can produce, until we reach the top of the triangle.