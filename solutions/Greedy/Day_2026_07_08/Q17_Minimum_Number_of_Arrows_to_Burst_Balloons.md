# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end point. You have a limited number of arrows, and each arrow can burst all the balloons in a certain range. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as a 2D vector, where each element is a vector of two integers representing the start and end points of a balloon. For example, `[[10,16],[2,8],[1,6],[7,12]]` represents four balloons with start and end points (10, 16), (2, 8), (1, 6), and (7, 12) respectively.

## Approach
The approach is to sort the balloons based on their end points and then use a greedy algorithm to find the minimum number of arrows needed. The idea is to always burst the balloon with the smallest end point first, and then move to the next balloon that is not burst by the current arrow.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0) return 0;
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        int arrows = 1;
        int pos = points[0][1];
        for (int i = 1; i < points.size(); i++) {
            if (points[i][0] > pos) {
                arrows++;
                pos = points[i][1];
            }
        }
        return arrows;
    }
};
```

## Test Cases
```
Input: [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Input: [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Input: [[1,6],[2,8],[7,12],[1,5]]
Output: 2
```

## Key Takeaways
- Sort the balloons based on their end points to ensure that we always burst the balloon with the smallest end point first.
- Use a greedy algorithm to find the minimum number of arrows needed by always moving to the next balloon that is not burst by the current arrow.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(1) since we only use a constant amount of space.