# Triangle Minimum Path

## Problem Statement
Given a triangle array where each row represents a level in the triangle, find the minimum path sum from top to bottom. Each step, you may move to an adjacent number in the row below. The triangle array is represented as a 2D vector where each sub-vector is a row in the triangle. For example, `[[2], [3,4], [6,5,7], [4,1,8,3]]` represents the following triangle:
```
   2
  3 4
 6 5 7
4 1 8 3
```
The minimum path sum from top to bottom is `2 + 3 + 5 + 1 = 11`. The input triangle will have at least one row and at most 100 rows. Each number in the triangle is between 1 and 100.

## Approach
The algorithm uses dynamic programming to build up a solution from the bottom of the triangle to the top. It iterates over each row from the second last to the first, updating each number to be the minimum sum it can achieve by moving down to the next row. The minimum path sum is stored in the top of the triangle after the algorithm finishes.

## Complexity
- Time: O(n^2)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
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
Input: [[2], [3,4], [6,5,7], [4,1,8,3]]
Output: 11
```

## Key Takeaways
- Dynamic programming can be used to solve problems that have overlapping subproblems.
- The key to this problem is to update each number in the triangle to be the minimum sum it can achieve by moving down to the next row.
- The space complexity is O(1) because we are modifying the input triangle in-place.