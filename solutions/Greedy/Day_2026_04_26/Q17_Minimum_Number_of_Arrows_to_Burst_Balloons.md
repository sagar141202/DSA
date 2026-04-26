# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and we want to burst them using the minimum number of arrows. Each balloon is represented by an interval `[start, end]`, and we can burst a balloon by shooting an arrow at any point within its interval. The goal is to find the minimum number of arrows needed to burst all the balloons. For example, given the intervals `[[10,16],[2,8],[1,6],[7,12]]`, we can burst all the balloons with 2 arrows by shooting at points 6 and 11.

## Approach
The algorithm uses a greedy approach, sorting the intervals by their end points and then iterating through them to find the minimum number of arrows needed. We always try to burst the current balloon with the previous arrow if possible.

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
        // Handle edge case
        if (points.empty()) return 0;
        
        // Sort the intervals by their end points
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        int arrows = 1;
        int pos = points[0][1];
        
        // Iterate through the sorted intervals
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon can't be burst by the previous arrow, increment the arrow count
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
- Sort the intervals by their end points to ensure that we can burst the maximum number of balloons with each arrow.
- Always try to burst the current balloon with the previous arrow if possible to minimize the number of arrows needed.
- The time complexity is O(n log n) due to the sorting step, and the space complexity is O(n) for the input intervals.