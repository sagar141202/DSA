# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level of the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number in the row below. The triangle array is represented as a 2D list of integers, where each inner list represents a row in the triangle. For example, `[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]` represents the following triangle:
```
    2
   3 4
  6 5 7
 4 1 8 3
```
The minimum path sum is the minimum sum of the numbers in the path from the top to the bottom. The constraints are that `1 <= triangle.length <= 200`, and `1 <= triangle[i].length <= 200`.

## Approach
The algorithm uses dynamic programming to build up a solution from the bottom of the triangle to the top. It starts by initializing the last row of the triangle as the minimum path sum to each node at that level. Then, it iterates up the triangle, updating the minimum path sum to each node based on the minimum path sum to its children.

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
        // Create a copy of the triangle to store the minimum path sum to each node
        vector<vector<int>> dp = triangle;
        
        // Iterate up the triangle, starting from the second last row
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the minimum path sum to each node based on the minimum path sum to its children
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum is stored in the top node
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
- Dynamic programming can be used to solve problems that have overlapping subproblems and optimal substructure.
- The time complexity of this solution is O(n^2) because we are iterating up the triangle, and the space complexity is also O(n^2) because we are creating a copy of the triangle to store the minimum path sum to each node.
- The minimum path sum is the minimum sum of the numbers in the path from the top to the bottom of the triangle.