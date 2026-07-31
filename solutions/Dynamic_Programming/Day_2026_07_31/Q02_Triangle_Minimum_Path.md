# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number in the row below. The triangle is represented as a 2D array where each sub-array is a level in the triangle. For example, given the triangle `[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]`, the minimum path sum is `2 + 3 + 5 + 1 = 11`. The triangle will have at least one row and each row will have at least one element.

## Approach
The problem can be solved using dynamic programming by iterating through the triangle from bottom to top and updating each element with the minimum sum it can produce. The minimum sum for each element is the element itself plus the minimum of the two elements directly below it.

## Complexity
- Time: O(n^2) where n is the number of rows in the triangle
- Space: O(1) if we modify the input triangle in-place, otherwise O(n^2) for a separate triangle to store the minimum sums

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        return triangle[0][0];
    }
};
```

## Test Cases
```
Input: [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
Output: 11
```

## Key Takeaways
- Dynamic programming can be used to efficiently solve problems that have overlapping subproblems.
- The triangle array can be modified in-place to reduce space complexity.
- The time complexity is O(n^2) due to the nested loops used to iterate through the triangle.