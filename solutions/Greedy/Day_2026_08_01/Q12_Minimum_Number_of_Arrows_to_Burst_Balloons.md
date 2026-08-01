# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end point. We have a limited number of arrows, and each arrow can burst all the balloons in a certain range. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as a 2D vector, where each sub-vector contains two integers representing the start and end points of a balloon. For example, `[[10,16],[2,8],[1,6],[7,12]]` represents four balloons with start and end points at (10,16), (2,8), (1,6), and (7,12) respectively.

## Approach
The approach is to sort the balloons by their end points and then iterate over them, using a greedy algorithm to find the minimum number of arrows needed. We always try to burst the current balloon with the previous arrow if possible.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.empty()) return 0;
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    int arrows = 1;
    int currEnd = points[0][1];
    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] > currEnd) {
            arrows++;
            currEnd = points[i][1];
        }
    }
    return arrows;
}
```

## Test Cases
```
Input: [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Input: [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Input: [[1,6],[2,8],[7,12],[1,5]]
Output: 2
```

## Key Takeaways
- Sort the balloons by their end points to ensure that we can burst the maximum number of balloons with each arrow.
- Use a greedy algorithm to find the minimum number of arrows needed, by always trying to burst the current balloon with the previous arrow if possible.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(1) as we only use a constant amount of space.