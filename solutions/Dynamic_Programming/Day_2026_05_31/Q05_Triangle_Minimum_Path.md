# Triangle Minimum Path

## Problem Statement
Given a triangle array where each element represents the minimum path sum from the top to the current element, find the minimum path sum from the top to the bottom of the triangle. The triangle is represented as an array of arrays, where each inner array represents a row in the triangle. For example, `[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]` represents the following triangle:
```
    2
   3 4
  6 5 7
 4 1 8 3
```
The minimum path sum from the top to the bottom is the minimum sum of the numbers in the path from the top element to one of the bottom elements. The path can only move either down to the left or down to the right.

## Approach
The problem can be solved using dynamic programming, where we start from the second last row and calculate the minimum path sum for each element. We then move up the triangle, updating the minimum path sum for each element based on the minimum path sum of its children.

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
        
        // Start from the second last row and move up
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the minimum path sum for each element
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum is stored in the top element
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
- The problem can be solved using dynamic programming, where we start from the second last row and move up.
- The minimum path sum for each element is updated based on the minimum path sum of its children.
- The time complexity is O(n^2) and the space complexity is O(n^2), where n is the number of rows in the triangle.