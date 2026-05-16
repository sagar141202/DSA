# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as pairs of integers, where the first integer represents the start of the interval and the second integer represents the end of the interval. For example, if we have intervals [[1, 2], [2, 3], [3, 4], [1, 3]], the maximum number of non-overlapping intervals is 2, which are [1, 2] and [3, 4] or [2, 3] and [1, 2] is not possible because [1,3] overlaps with both. The goal is to write a function that takes a list of intervals as input and returns the maximum number of non-overlapping intervals.

## Approach
The algorithm sorts the intervals based on their end points and then iterates over them, selecting the non-overlapping ones. This approach works because once an interval is selected, all other intervals that overlap with it can be skipped. The next interval to be selected will be the one with the smallest end point that does not overlap with the previously selected interval.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        if (intervals.size() == 0) {
            return 0;
        }

        // Sort the intervals based on their end points
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });

        int count = 1;
        int end = intervals[0][1];

        // Iterate over the intervals and select the non-overlapping ones
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i][0] >= end) {
                count++;
                end = intervals[i][1];
            }
        }

        // The maximum number of non-overlapping intervals is the total number of intervals minus the number of overlapping intervals
        return intervals.size() - count;
    }
};
```

## Test Cases
```
Input: [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Input: [[1, 2], [1, 2], [1, 2]]
Output: 2
Input: [[1, 2], [2, 3]]
Output: 0
```

## Key Takeaways
- Sort the intervals based on their end points to efficiently select the non-overlapping ones.
- Use a greedy approach to select the non-overlapping intervals, as this problem has the optimal substructure property.
- The time complexity of the solution is O(n log n) due to the sorting step, and the space complexity is O(n) for the input intervals.