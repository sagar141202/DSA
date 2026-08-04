# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level of the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number in the row below. The triangle array is represented as a 2D array, and the minimum path sum is the sum of the numbers in the path. For example, given the triangle `[[2], [3,4], [6,5,7], [4,1,8,3]]`, the minimum path sum is `2 + 3 + 5 + 1 = 11`. The triangle array will have at most 200 rows, and each row will have at most 200 elements.

## Approach
We will use dynamic programming to solve this problem by maintaining an array of minimum path sums at each level of the triangle. We start from the second last row and move upwards, updating the minimum path sum at each position by adding the minimum of the two numbers below it. This approach ensures that we consider all possible paths and find the minimum one.

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
        
        // Start from the second last row and move upwards
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
- Use dynamic programming to maintain an array of minimum path sums at each level of the triangle.
- Start from the second last row and move upwards to update the minimum path sum at each position.
- The minimum path sum is stored at the top of the triangle after the dynamic programming process.