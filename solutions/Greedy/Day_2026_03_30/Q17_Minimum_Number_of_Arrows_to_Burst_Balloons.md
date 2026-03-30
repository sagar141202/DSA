# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. We are given an array of intervals, where each interval represents the start and end position of a balloon. The task is to find the minimum number of arrows required to burst all the balloons. An arrow can burst a balloon if it is shot at a position that is within the range of the balloon. If two balloons overlap, we can burst them with a single arrow. The input array will contain intervals of the form [start, end], where start and end are integers. The array will not be empty, and the length of the array will be in the range [1, 10^4]. The start and end positions will be in the range [0, 10^6].

## Approach
The approach is to sort the intervals based on their end positions and then iterate through the sorted intervals, keeping track of the end position of the last burst balloon. If the current balloon does not overlap with the last burst balloon, we increment the count of arrows and update the last burst position.

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
        if (points.empty()) return 0;
        
        // Sort the intervals based on their end positions
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        
        int arrows = 1;
        int lastEnd = points[0][1];
        
        // Iterate through the sorted intervals
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon does not overlap with the last burst balloon
            if (points[i][0] > lastEnd) {
                // Increment the count of arrows and update the last burst position
                arrows++;
                lastEnd = points[i][1];
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
Input: [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Input: [[1,6],[2,8],[7,12],[1,5]]
Output: 2
```

## Key Takeaways
- Sort the intervals based on their end positions to ensure that we burst the balloons in the correct order.
- Keep track of the end position of the last burst balloon to determine if the current balloon overlaps with it.
- Increment the count of arrows only when a new balloon does not overlap with the last burst balloon.