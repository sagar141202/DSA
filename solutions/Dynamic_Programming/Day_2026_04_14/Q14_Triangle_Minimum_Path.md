# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number in the row below. The triangle array is represented as a 2D array, and the input will be a vector of vectors. For example, if the input is `[[2],[3,4],[6,5,7],[4,1,8,3]]`, then the minimum path sum is `11` (2 + 3 + 5 + 1).

## Approach
The problem can be solved using dynamic programming, where we start from the bottom of the triangle and work our way up. At each level, we calculate the minimum path sum to each node by taking the minimum of the two nodes below it and adding the current node's value. This approach ensures that we consider all possible paths and find the minimum sum.

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
                // Calculate the minimum path sum to each node by taking the minimum of the two nodes below it and adding the current node's value
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum is stored in the top node of the triangle
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
- Start from the bottom of the triangle and work your way up to calculate the minimum path sum.
- Use dynamic programming to store the minimum path sums at each level and avoid redundant calculations.
- The minimum path sum is stored in the top node of the triangle after the dynamic programming process.