# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. You have a limited number of arrows, and each arrow can burst a number of balloons if they are overlapping. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as intervals, where each interval is of the form [start, end]. Two balloons are considered overlapping if there exists a point that is within both intervals. For example, the intervals [1, 2] and [2, 3] are overlapping because the point 2 is within both intervals.

## Approach
The problem can be solved using a greedy approach by sorting the balloons based on their end positions and then iterating over them to find the minimum number of arrows needed. The idea is to always try to burst the current balloon with the previous arrow if possible.

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
        if (points.size() == 0) {
            return 0;
        }
        
        // Sort the balloons based on their end positions
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int arrows = 1;
        int currEnd = points[0][1];
        
        // Iterate over the sorted balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon does not overlap with the previous one, increment the arrow count
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
Input: [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Input: [[1,6],[2,8],[7,12],[1,5]]
Output: 2
```

## Key Takeaways
- Always try to burst the current balloon with the previous arrow if possible to minimize the number of arrows needed.
- Sorting the balloons based on their end positions allows us to efficiently find the minimum number of arrows needed.
- The time complexity of the solution is O(n log n) due to the sorting step, where n is the number of balloons.