# Triangle Minimum Path

## Problem Statement
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below. The triangle is represented as a 2D array where each sub-array represents a row in the triangle. For example, given the following triangle:
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
The minimum path sum from top to bottom is `2 + 3 + 5 + 1 = 11`. The constraints are: `1 <= triangle.length <= 200`, and `triangle[i].length == i + 1`.

## Approach
The algorithm uses dynamic programming to build up the minimum path sum from the bottom of the triangle to the top. It starts from the second last row and for each element, it calculates the minimum sum by adding the current element with the minimum of the two elements directly below it.

## Complexity
- Time: O(n^2)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        // Start from the second last row
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // Update the current element with the minimum sum
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        // The minimum path sum is stored in the top element
        return triangle[0][0];
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
- Use dynamic programming to solve problems that have overlapping subproblems.
- The minimum path sum can be calculated by starting from the bottom of the triangle and moving up.
- The space complexity can be optimized to O(1) by modifying the input triangle in-place.