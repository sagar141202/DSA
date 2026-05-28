# Minimum Number of Arrows to Burst Balloons

## Problem Statement
Given a 2D vector `points` where `points[i] = [x_start, x_end]` represents a balloon, where `x_start` and `x_end` are integers, find the minimum number of arrows that must be shot to burst all balloons. If there are multiple balloons in the same position, only one arrow is needed to burst them. The input array will be sorted by `x_start` in ascending order. The constraints are: `1 <= points.length <= 10^5` and `points[i].length == 2`. For example, given `points = [[10,16],[2,8],[1,6],[7,12]]`, the output should be `2` because the minimum number of arrows needed to burst all balloons is `2`.

## Approach
The approach is to use a greedy algorithm by sorting the balloons by their end points and then iterating through the sorted list, using the end point of the previous balloon as the position for the next arrow. This ensures that the minimum number of arrows are used to burst all balloons. The key idea is to always try to burst the next balloon with the current arrow if possible.

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
    int arrow = 1;
    int pos = points[0][1];
    for (int i = 1; i < points.size(); i++) {
        if (points[i][0] > pos) {
            arrow++;
            pos = points[i][1];
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
Input: [[1,6],[2,8],[7,12],[1,5]]
Output: 2
```

## Key Takeaways
- The greedy algorithm works by always trying to burst the next balloon with the current arrow if possible.
- Sorting the balloons by their end points is crucial for the algorithm to work correctly.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(1) as no additional space is used.