# Triangle Minimum Path

## Problem Statement
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. The triangle is represented as a 2D array, where each sub-array represents a row in the triangle. For example, `[[2], [3,4], [6,5,7], [4,1,8,3]]` represents the following triangle: 
```
    2
   3 4
  6 5 7
 4 1 8 3
```
The minimum path sum from top to bottom is `2 + 3 + 5 + 1 = 11`. The constraints are: `1 <= triangle.length <= 200`, and `triangle[i].length == i + 1`.

## Approach
The algorithm uses dynamic programming to build up a solution by computing the minimum path sum to each cell in the triangle. The minimum path sum to a cell is the minimum of the path sums to the cells above and to the left and right, plus the value of the current cell.

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
        
        // Fill in the dp table in a bottom-up manner
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // The minimum path sum to a cell is the minimum of the path sums to the cells below and to the left and right, plus the value of the current cell
                dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1]);
            }
        }
        
        // The minimum path sum from top to bottom is stored in the top cell of the dp table
        return dp[0][0];
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
- Use dynamic programming to solve problems that have overlapping sub-problems and optimal sub-structure.
- The time complexity of the solution is O(n^2) because we need to fill in the dp table, which has n^2 cells.
- The space complexity of the solution is O(n^2) because we need to store the dp table, which has n^2 cells.