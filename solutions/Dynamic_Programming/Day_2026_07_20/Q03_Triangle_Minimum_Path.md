# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level of the triangle, find the minimum path sum from top to bottom. Each step, you may move to the adjacent numbers on the row below. The triangle array is represented as a 2D array, where each sub-array is a row in the triangle. For example, given the triangle `[[2],[3,4],[6,5,7],[4,1,8,3]]`, the minimum path sum is `2 + 3 + 5 + 1 = 11`. The input triangle will have at least one row and at most 100 rows, with each row having one more element than the previous row.

## Approach
The problem can be solved using dynamic programming by starting from the second last row and updating the values of the elements in the current row with the minimum sum of the element and its adjacent elements in the next row. This process continues until the first row is reached, which will have the minimum path sum.

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
        // start from the second last row
        for (int i = n - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].size(); j++) {
                // update the value of the current element with the minimum sum
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        // the minimum path sum is stored in the first row
        return triangle[0][0];
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
- The dynamic programming approach is used to solve the problem efficiently.
- The time complexity is O(n^2) due to the nested loops used to update the values of the elements in the triangle.
- The space complexity is O(1) as no extra space is used, the input triangle is modified in-place.