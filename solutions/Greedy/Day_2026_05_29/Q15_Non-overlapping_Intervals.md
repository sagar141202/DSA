# Non-overlapping Intervals

## Problem Statement
Given a collection of intervals, find the maximum number of non-overlapping intervals that can be selected. The intervals are represented as pairs of integers, where the first integer is the start time and the second integer is the end time. Two intervals are considered non-overlapping if the end time of the first interval is less than or equal to the start time of the second interval. For example, given the intervals [[1, 2], [2, 3], [3, 4], [1, 3]], the maximum number of non-overlapping intervals that can be selected is 2, which are [1, 2] and [2, 3] or [3, 4]. The intervals are not guaranteed to be sorted.

## Approach
The algorithm uses a greedy approach, sorting the intervals by their end times and then selecting the interval with the smallest end time that does not overlap with the previously selected interval. This approach ensures that the maximum number of non-overlapping intervals are selected. The intuition behind this is that by selecting the interval with the smallest end time, we are leaving the most room for the next interval to be selected.

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
        // If the intervals list is empty, return 0
        if (intervals.size() == 0) return 0;

        // Sort the intervals based on their end time
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            return a[1] < b[1];
        });

        // Initialize the count of non-overlapping intervals and the end time of the last non-overlapping interval
        int count = 1;
        int lastEndTime = intervals[0][1];

        // Iterate over the intervals
        for (int i = 1; i < intervals.size(); i++) {
            // If the current interval does not overlap with the last non-overlapping interval, increment the count and update the last end time
            if (intervals[i][0] >= lastEndTime) {
                count++;
                lastEndTime = intervals[i][1];
            }
        }

        // The number of intervals to remove is the total number of intervals minus the number of non-overlapping intervals
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
- The greedy approach is used to solve this problem, which involves sorting the intervals by their end times and then selecting the interval with the smallest end time that does not overlap with the previously selected interval.
- The time complexity of the solution is O(n log n) due to the sorting of the intervals, where n is the number of intervals.
- The space complexity of the solution is O(n) if the input intervals are not sorted, otherwise it is O(1) if the input intervals are already sorted.