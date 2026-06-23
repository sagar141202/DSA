# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level of the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number in the row below. The triangle array will have at least one row and at most 20 rows, and each row will have one more element than its row number (i.e., the first row will have one element, the second row will have two elements, and so on). The elements in the triangle array will be in the range [-100, 100] and will not be empty.

## Approach
The algorithm uses dynamic programming to build up a solution by computing the minimum path sum to each element in the triangle. It starts from the second last row and iteratively updates the minimum path sum to each element in the current row.

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
        // Create a copy of the triangle to store the minimum path sum to each element
        vector<vector<int>> dp = triangle;
        
        // Start from the second last row and iteratively update the minimum path sum
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the minimum path sum to each element in the current row
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
Input: [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
```

## Key Takeaways
- Use dynamic programming to break down the problem into smaller sub-problems and store the solutions to sub-problems to avoid redundant computation.
- The time complexity is O(n^2) where n is the number of rows in the triangle, and the space complexity is also O(n^2) for storing the minimum path sum to each element.