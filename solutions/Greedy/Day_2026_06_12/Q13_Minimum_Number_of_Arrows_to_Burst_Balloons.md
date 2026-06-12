# Minimum Number of Arrows to Burst Balloons

## Problem Statement
Given a 2D vector `points` where `points[i] = [x_start, x_end]` represents a balloon, where `x_start` and `x_end` denote the start and end coordinates of the balloon. The goal is to find the minimum number of arrows required to burst all the balloons. If there are two balloons with some overlapping part, we can burst them with a single arrow. The input array `points` is guaranteed to be non-empty, and `x_start` is less than or equal to `x_end` for all balloons.

## Approach
The algorithm involves sorting the balloons based on their end points and then iterating over the sorted list to find the minimum number of arrows required. We use a greedy approach, always trying to burst the current balloon with the previous one if possible.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    // Sort the points based on their end coordinates
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    
    int arrows = 1;  // Initialize the number of arrows
    int end = points[0][1];  // Initialize the end point of the current arrow
    
    // Iterate over the sorted points
    for (int i = 1; i < points.size(); i++) {
        // If the current balloon does not overlap with the current arrow, increment the number of arrows
        if (points[i][0] > end) {
            arrows++;
            end = points[i][1];
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
- Sort the balloons based on their end points to ensure that we can burst them with the minimum number of arrows.
- Use a greedy approach to always try to burst the current balloon with the previous one if possible.
- The time complexity is O(n log n) due to the sorting operation, and the space complexity is O(1) as we only use a constant amount of space.