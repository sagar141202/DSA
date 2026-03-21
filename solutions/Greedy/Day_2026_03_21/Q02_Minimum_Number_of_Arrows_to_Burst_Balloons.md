# Minimum Number of Arrows to Burst Balloons

## Problem Statement
There are a number of balloons flying in the air, and each balloon has a start and end position. We are given a list of intervals representing the start and end positions of the balloons. The goal is to find the minimum number of arrows needed to burst all the balloons. An arrow can burst all the balloons in a particular interval if the arrow is shot at a position that is within the interval of all the balloons. The input is a 2D array `points` where `points[i] = [left, right]`, and `left` and `right` represent the start and end positions of the `i-th` balloon. The constraint is that `0 <= left <= right <= 10^4` and `0 <= points.length <= 10^4`.

## Approach
The algorithm sorts the intervals based on their end positions and then iterates over the sorted intervals, using a greedy approach to find the minimum number of arrows needed. The idea is to always try to burst the current balloon with the previous arrow if possible. If not, a new arrow is needed.

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
        if (points.size() == 0) return 0;
        
        // Sort the intervals based on their end positions
        sort(points.begin(), points.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });
        
        int arrows = 1;
        int currEnd = points[0][1];
        
        // Iterate over the sorted intervals
        for (int i = 1; i < points.size(); i++) {
            // If the current balloon cannot be burst by the previous arrow, a new arrow is needed
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
- Sorting the intervals based on their end positions is crucial for the greedy approach to work.
- The algorithm always tries to burst the current balloon with the previous arrow if possible, which ensures the minimum number of arrows needed.
- The time complexity is O(n log n) due to the sorting operation, and the space complexity is O(1) as no extra space is used.