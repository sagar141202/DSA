# Triangle Minimum Path

## Problem Statement
Given a triangle array where each sub-array represents a row in the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number in the row below. The triangle array will have at least one row and at most 100 rows, with each row having one more element than the previous row. The elements in the triangle array will be in the range [-100, 100]. For example, given the triangle `[[2], [3,4], [6,5,7], [4,1,8,3]]`, the minimum path sum is `11`, which is achieved by the path `2 -> 3 -> 5 -> 1`.

## Approach
The algorithm uses dynamic programming to build up the minimum path sum from the bottom of the triangle to the top. It iterates over each row from the second last to the first, updating the current row's elements with the minimum sum of the current element and the two elements directly below it. This process continues until the minimum path sum is determined at the top of the triangle.

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
        
        // Iterate over each row from the second last to the first
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the current row's elements with the minimum sum of the current element and the two elements directly below it
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
```

## Key Takeaways
- The dynamic programming approach allows us to break down the problem into smaller sub-problems and store the solutions to these sub-problems to avoid redundant computation.
- The time complexity of the solution is O(n^2), where n is the number of rows in the triangle, because we are iterating over each element in the triangle once.
- The space complexity of the solution is O(n^2) because we are creating a copy of the input triangle to store the minimum path sums.