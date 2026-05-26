# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and we have a certain number of arrows to burst them. Each balloon has a start and end point, and if an arrow is shot at a point within the range of a balloon, it will burst. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented by a 2D vector `points`, where `points[i] = [start, end]`. The balloons are non-overlapping, and the start point of each balloon is less than its end point.

## Approach
The approach is to sort the balloons by their end points and then iterate over them, using a greedy strategy to find the minimum number of arrows needed. We always try to burst the current balloon with the same arrow that was used to burst the previous balloon, if possible.

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
        if (points.size() == 0) {
            return 0;
        }
        
        // Sort the points by their end value
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        
        int arrows = 1;
        int currEnd = points[0][1];
        
        // Iterate over the points
        for (int i = 1; i < points.size(); i++) {
            // If the current point's start value is greater than the current end value,
            // we need a new arrow
            if (points[i][0] > currEnd) {
                arrows++;
                currEnd = points[i][1];
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
```

## Key Takeaways
- Sort the balloons by their end points to ensure that we can burst as many balloons as possible with each arrow.
- Use a greedy strategy to find the minimum number of arrows needed, by always trying to burst the current balloon with the same arrow that was used to burst the previous balloon, if possible.