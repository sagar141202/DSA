# Triangle Minimum Path

## Problem Statement
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. The triangle is represented as a 2D array, where each sub-array represents a row in the triangle. For example, given the triangle `[[2], [3,4], [6,5,7], [4,1,8,3]]`, the minimum path sum is `11` (i.e., `2 + 3 + 5 + 1 = 11`).

## Approach
The problem can be solved using dynamic programming by iterating over each row in the triangle and updating the minimum path sum at each position. The minimum path sum at each position is the minimum of the path sums from the two positions directly above it, plus the value at the current position.

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
        
        // Iterate over each row in the triangle from the second last row to the first row
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the minimum path sum at each position
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
Input: [[-10]]
Output: -10
```

## Key Takeaways
- Use dynamic programming to solve the problem by iterating over each row in the triangle and updating the minimum path sum at each position.
- The minimum path sum at each position is the minimum of the path sums from the two positions directly above it, plus the value at the current position.
- The time complexity of the solution is O(n^2), where n is the number of rows in the triangle.