# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. We are given a 2D array `points` where `points[i] = [start, end]` represents the start and end position of the `i-th` balloon. We need to find the minimum number of arrows required to burst all the balloons. If a balloon is hit by an arrow, it will burst and no longer exist. Two balloons can be burst by a single arrow if they overlap.

## Approach
The approach is to sort the balloons based on their end position and then use a greedy algorithm to find the minimum number of arrows required. We always try to burst the current balloon with the same arrow that was used to burst the previous balloon if they overlap.

## Complexity
- Time: O(n log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findMinArrowShots(vector<vector<int>>& points) {
    if (points.size() == 0) return 0;
    
    // Sort the points based on their end position
    sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[1] < b[1];
    });
    
    int arrowCount = 1;
    int currentEnd = points[0][1];
    
    for (int i = 1; i < points.size(); i++) {
        // If the current balloon does not overlap with the previous one, we need a new arrow
        if (points[i][0] > currentEnd) {
            arrowCount++;
            currentEnd = points[i][1];
        }
    }
    
    return arrowCount;
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
- Sort the points based on their end position to ensure that we always try to burst the current balloon with the same arrow that was used to burst the previous balloon if they overlap.
- Use a greedy algorithm to find the minimum number of arrows required.
- We only need to keep track of the end position of the previous balloon to determine if the current balloon can be burst by the same arrow.