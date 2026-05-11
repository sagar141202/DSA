# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. The triangle array is represented as a 2D array, where each sub-array is a row in the triangle. For example, given the triangle `[[2], [3,4], [6,5,7], [4,1,8,3]]`, the minimum path sum is `11` (i.e., `2 + 3 + 5 + 1 = 11`).

## Approach
The algorithm uses dynamic programming to build up a solution from the bottom of the triangle to the top. It starts by initializing the last row of the triangle as the base case, then iteratively updates each element in the triangle to be the minimum sum of the paths from its children.

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
        // Create a copy of the triangle to store the minimum path sums
        vector<vector<int>> dp = triangle;
        
        // Start from the second last row and move upwards
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the minimum path sum for each element
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum is stored in the top element of the triangle
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
- Use dynamic programming to solve problems that have overlapping subproblems.
- Initialize the base case carefully to avoid errors.
- Use a bottom-up approach to build up the solution from the base case.