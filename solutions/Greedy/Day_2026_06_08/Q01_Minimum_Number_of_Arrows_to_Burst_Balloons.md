# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. You have a certain number of arrows, and you want to burst as many balloons as possible with the minimum number of arrows. The balloons are represented by intervals on the x-axis, where each interval is of the form [start, end]. If an arrow is shot at position x, all balloons that contain the point x will be burst. The goal is to find the minimum number of arrows needed to burst all balloons. For example, given the intervals [[10,16],[2,8],[1,6],[7,12]], the minimum number of arrows needed is 2, by shooting at positions 6 and 11.

## Approach
The approach is to sort the balloons by their end positions and then use a greedy algorithm to find the minimum number of arrows. We always try to burst the balloon with the earliest end position first.

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
        // If there are no balloons, we don't need any arrows
        if (points.empty()) return 0;
        
        // Sort the balloons by their end positions
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        
        // Initialize the number of arrows and the position of the last arrow
        int arrows = 1;
        int lastArrow = points[0][1];
        
        // Iterate over the balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon is not burst by the last arrow, we need a new arrow
            if (points[i][0] > lastArrow) {
                arrows++;
                lastArrow = points[i][1];
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
- Sort the balloons by their end positions to ensure that we burst the balloon with the earliest end position first.
- Use a greedy algorithm to find the minimum number of arrows, by always trying to burst the current balloon with the last arrow.
- Keep track of the position of the last arrow to determine if the current balloon is burst by the last arrow.