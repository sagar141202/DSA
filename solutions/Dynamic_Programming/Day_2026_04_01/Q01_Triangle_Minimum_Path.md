# Triangle Minimum Path

## Problem Statement
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. The triangle is represented as a 2D array, where each sub-array represents a row in the triangle. For example, `[[2], [3,4], [6,5,7], [4,1,8,3]]` represents the following triangle: 
```
   2
  3 4
 6 5 7
4 1 8 3
```
The minimum path sum from top to bottom is `2 + 3 + 5 + 1 = 11`.

## Approach
We will use dynamic programming to build up a solution from the bottom of the triangle to the top. At each step, we choose the minimum sum of the two numbers below it.

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
        
        // Start from the second last row and move upwards
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
Input: [[2], [3,4], [6,5,7], [4,1,8,3]]
Output: 11
Input: [[-10]]
Output: -10
```

## Key Takeaways
- Use dynamic programming to break down the problem into smaller sub-problems and store the results in a table.
- The minimum path sum can be calculated by iterating through the triangle from the bottom up and choosing the minimum sum of the two numbers below each element.
- The time complexity of this solution is O(n^2), where n is the number of rows in the triangle.