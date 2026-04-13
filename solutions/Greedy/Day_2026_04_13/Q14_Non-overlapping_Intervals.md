# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals. The intervals are represented as a vector of pairs, where each pair contains two integers representing the start and end of an interval. The goal is to select the maximum number of intervals such that no two intervals overlap. For example, given the intervals [(1, 2), (2, 3), (3, 4), (1, 3)], the maximum number of non-overlapping intervals is 2, which can be achieved by selecting the intervals (1, 2) and (3, 4).

## Approach
The algorithm sorts the intervals based on their end points and then iterates through the sorted intervals, selecting the non-overlapping ones. This approach ensures that the maximum number of non-overlapping intervals is selected. The key idea is to always choose the interval with the smallest end point that does not overlap with the previously selected interval.

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
        // If the input vector is empty, return 0
        if (intervals.empty()) return 0;

        // Sort the intervals based on their end points
        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1];
        });

        // Initialize the count of non-overlapping intervals and the end point of the last selected interval
        int count = 1;
        int lastEnd = intervals[0][1];

        // Iterate through the sorted intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current interval does not overlap with the last selected interval, increment the count and update the last end point
            if (intervals[i][0] >= lastEnd) {
                count++;
                lastEnd = intervals[i][1];
            }
        }

        // Return the maximum number of non-overlapping intervals
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
- The greedy approach is used to solve the problem by always choosing the interval with the smallest end point that does not overlap with the previously selected interval.
- The time complexity is O(n log n) due to the sorting of intervals.
- The space complexity is O(n) for storing the input intervals.