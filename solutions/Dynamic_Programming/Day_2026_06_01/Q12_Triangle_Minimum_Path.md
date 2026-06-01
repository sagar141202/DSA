# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number in the row below. The triangle array will have at least one row and at most 20 rows, with each row having one more element than its row number (i.e., the first row has one element, the second row has two elements, and so on). The elements in the triangle array are in the range [-100, 100] and all inputs are valid.

## Approach
The problem can be solved using dynamic programming by iterating through the triangle from bottom to top and updating each element with the minimum sum of the current element and its adjacent elements in the row below. This approach ensures that we consider all possible paths and choose the one with the minimum sum.

## Complexity
- Time: O(n^2) where n is the number of rows in the triangle
- Space: O(1) if we modify the input triangle in-place, or O(n^2) if we create a separate 2D array to store the minimum sums

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
                // Update each element with the minimum sum of the current element and its adjacent elements
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]);
            }
        }
        // The minimum path sum is stored in the top element of the triangle
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
- We can solve the problem using dynamic programming by iterating through the triangle from bottom to top.
- We need to consider all possible paths and choose the one with the minimum sum.
- The time complexity is O(n^2) where n is the number of rows in the triangle, and the space complexity is O(1) if we modify the input triangle in-place.