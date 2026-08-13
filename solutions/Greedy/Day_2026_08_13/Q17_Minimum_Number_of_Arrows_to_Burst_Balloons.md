# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and we want to burst them using the minimum number of arrows. Each balloon has a start and end point, and if an arrow is shot at a point that is within the range of a balloon, it will burst. Given the start and end points of the balloons, find the minimum number of arrows needed to burst all the balloons. The balloons are represented as intervals, e.g., [[10,16],[2,8],[1,6],[7,12]]. The input is a 2D vector of integers, where each inner vector represents a balloon. The output should be the minimum number of arrows needed.

## Approach
The approach is to sort the balloons by their end points, then use a greedy algorithm to find the minimum number of arrows. We start with the first balloon and try to burst as many balloons as possible with one arrow.

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
        // If there are no balloons, return 0
        if (points.size() == 0) return 0;
        
        // Sort the balloons by their end points
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int arrows = 1;
        int pos = points[0][1];
        
        // Iterate over the balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon is not burst by the previous arrow, increment the arrow count
            if (points[i][0] > pos) {
                arrows++;
                pos = points[i][1];
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
- Sort the balloons by their end points to ensure that we burst as many balloons as possible with one arrow.
- Use a greedy algorithm to find the minimum number of arrows.
- The time complexity is O(n log n) due to the sorting step.