# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number (to the left or right). The triangle array will have at least one row and will not be empty. For example, given the following triangle: 
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum is 2 + 3 + 5 + 1 = 11.

## Approach
The solution uses dynamic programming to build up a table of minimum path sums. It starts from the second last row and works its way up to the top, at each step choosing the minimum path sum of the two adjacent numbers in the row below. The minimum path sum of the top number is then the minimum path sum of the entire triangle.

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
                // Update the minimum path sum for the current number
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum of the top number is the minimum path sum of the entire triangle
        return dp[0][0];
    }
};
```

## Test Cases
```
Input: [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Output: 11
```

## Key Takeaways
- Use dynamic programming to build up a table of minimum path sums.
- Start from the second last row and work your way up to the top.
- At each step, choose the minimum path sum of the two adjacent numbers in the row below.