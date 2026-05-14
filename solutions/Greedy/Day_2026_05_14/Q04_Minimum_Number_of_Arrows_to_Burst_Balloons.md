# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons floating in the air, and each balloon has a start and end position. You have a limited number of arrows, and each arrow can burst a number of balloons if they overlap. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as intervals, where each interval is of the form [start, end]. Two balloons overlap if there is a point that is within both intervals.

## Approach
The problem can be solved using a greedy algorithm by first sorting the balloons by their end points. Then, we iterate through the sorted list and use an arrow to burst the current balloon and all the balloons that overlap with it.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        if (points.size() == 0) return 0;
        
        // Sort the balloons by their end points
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int arrows = 1;
        int currentEnd = points[0][1];
        
        // Iterate through the sorted list and use an arrow to burst the current balloon and all the balloons that overlap with it
        for (int i = 1; i < points.size(); i++) {
            if (points[i][0] > currentEnd) {
                arrows++;
                currentEnd = points[i][1];
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
- Sort the balloons by their end points to ensure that we use the minimum number of arrows.
- Use a greedy approach to iterate through the sorted list and burst the balloons that overlap with the current balloon.
- Keep track of the end point of the current balloon to determine if the next balloon overlaps with it.