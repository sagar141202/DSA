# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from the top to the bottom. Each step, you may move to an adjacent number in the row below. The triangle array is represented as a 2D array, where the i-th row has i+1 elements. The input triangle will have at least one row and at most 100 rows. The values in the triangle will be between -100 and 100. For example, given the triangle `[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]`, the minimum path sum is `11`, which is `2 + 3 + 5 + 1`.

## Approach
The problem can be solved using dynamic programming, where we start from the bottom of the triangle and work our way up, updating the minimum path sum at each step. We use a bottom-up approach to avoid redundant calculations. The algorithm iterates over each element in the triangle, updating its value to be the minimum sum of the path from the top to that element.

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
        
        // Start from the second last row and work our way up
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the minimum path sum for each element
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum is stored in the top element of the dp array
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
- The problem can be solved using dynamic programming with a bottom-up approach.
- The time complexity is O(n^2), where n is the number of rows in the triangle.
- The space complexity is O(n^2), as we need to store the minimum path sum for each element in the triangle.