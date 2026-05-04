# Triangle Minimum Path

## Problem Statement
Given a triangle array where each sub-array represents a row in the triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. The first row has one number, the second row has two numbers, and so on. The last row has n numbers. For example, given the following triangle: `[ [2], [3,4], [6,5,7], [4,1,8,3] ]`, the minimum path sum is `2 + 3 + 5 + 1 = 11`.

## Approach
The problem can be solved using dynamic programming by maintaining an array to store the minimum path sum at each position. We start from the second last row and update the values of the above rows based on the minimum sum of the two numbers below it. This process is repeated until we reach the top of the triangle.

## Complexity
- Time: O(n^2)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        // Create a copy of the last row to store the minimum path sum
        vector<int> dp = triangle.back();
        
        // Iterate over each row from the second last to the first
        for (int i = n - 2; i >= 0; i--) {
            // Iterate over each number in the current row
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the minimum path sum by adding the minimum of the two numbers below
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1]);
            }
        }
        
        // The minimum path sum is stored in the first element of dp
        return dp[0];
    }
};
```

## Test Cases
```
Input: [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Input: [[-10]]
Output: -10
```

## Key Takeaways
- The dynamic programming approach is used to break down the problem into smaller sub-problems and store the solutions to sub-problems to avoid redundant computation.
- The time complexity is O(n^2) due to the nested loops used to iterate over the rows and numbers in the triangle.
- The space complexity is O(n) as we need to store the minimum path sum for each number in the last row.