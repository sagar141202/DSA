# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from the top to the bottom. Each step, you may move to an adjacent number in the row below. The triangle array is represented as a 2D array, where each element is a non-negative integer. For example, given the triangle `[[2], [3,4], [6,5,7], [4,1,8,3]]`, the minimum path sum is `2 + 3 + 5 + 1 = 11`. The triangle array will have at most 200 rows and each row will have at most 200 elements.

## Approach
The algorithm uses dynamic programming to build up a solution from the bottom of the triangle to the top. It iterates over each row, updating the minimum path sum for each element based on the minimum path sum of its children in the row below. The minimum path sum is then returned as the value of the top element.

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
        vector<vector<int>> dp = triangle;
        
        // iterate from second last row to first row
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // update the minimum path sum for each element
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // return the minimum path sum
        return dp[0][0];
    }
};
```

## Test Cases
```
Input: [[2], [3,4], [6,5,7], [4,1,8,3]]
Output: 11
```

## Key Takeaways
- Use dynamic programming to solve problems that have overlapping subproblems.
- The time complexity is O(n^2) because we are iterating over each element in the triangle array.
- The space complexity is O(n^2) because we are storing the minimum path sum for each element in the triangle array.