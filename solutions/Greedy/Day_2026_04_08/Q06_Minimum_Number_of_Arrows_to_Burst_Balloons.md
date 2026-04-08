# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. You have a certain number of arrows, and each arrow can burst a balloon. The goal is to find the minimum number of arrows needed to burst all the balloons. The balloons are represented as intervals [start, end], where start and end are the start and end positions of the balloon. Two balloons can be burst by one arrow if they have any overlap.

## Approach
The approach is to sort the balloons by their end positions and then iterate over the sorted balloons, using a greedy algorithm to find the minimum number of arrows. The idea is to always try to burst the current balloon with the previous arrow.

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
        // If there are no balloons, return 0
        if (points.size() == 0) return 0;
        
        // Sort the balloons by their end positions
        sort(points.begin(), points.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });
        
        // Initialize the count of arrows and the position of the last arrow
        int count = 1;
        int last_pos = points[0][1];
        
        // Iterate over the sorted balloons
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon does not overlap with the last arrow, increment the count and update the last position
            if (points[i][0] > last_pos) {
                count++;
                last_pos = points[i][1];
            }
        }
        
        // Return the minimum number of arrows
        return count;
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
- Sort the balloons by their end positions to ensure that we can burst as many balloons as possible with each arrow.
- Use a greedy algorithm to find the minimum number of arrows, always trying to burst the current balloon with the previous arrow.
- The time complexity is O(n log n) due to the sorting, and the space complexity is O(n) for the sorting.