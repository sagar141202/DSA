# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end point. You have a certain number of arrows, and each arrow can burst all the balloons in a certain range. The goal is to find the minimum number of arrows needed to burst all the balloons. The input is a 2D vector where each sub-vector contains two integers representing the start and end points of a balloon. The balloons are guaranteed to be non-overlapping, but they may be adjacent.

## Approach
The approach is to sort the balloons by their end points and then use a greedy algorithm to find the minimum number of arrows. We always try to burst the balloon with the smallest end point first.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) return 0;
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    int arrow = 1;
    int pos = points[0][1];
    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] > pos) {
            pos = points[i][1];
            arrow++;
        }
    }
    return arrow;
}
```

## Test Cases
```
Input: [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Input: [[1,2],[2,3],[3,4],[4,5]]
Output: 2
```

## Key Takeaways
- The key to this problem is to sort the balloons by their end points.
- We use a greedy algorithm to find the minimum number of arrows.
- The time complexity is O(n log n) due to the sorting, and the space complexity is O(n) for the sorting in the worst case.